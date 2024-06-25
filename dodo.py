import glob
import shutil
from doit.tools import create_folder
import tomllib
from doit.task import clean_targets

DOIT_CONFIG = {'default_tasks': ['all']}
PODEST = 'TaskTracker/po'


def task_pot():
    """Re-create .pot ."""
    return {
            'actions': ['pybabel extract -o msg.pot TaskTracker'],
            'file_dep': glob.glob('TaskTracker/*.py'),
            'targets': ['msg.pot'],
           }


def task_po():
    """Update translations."""
    return {
            'actions': ['pybabel update --ignore-pot-creation-date -D msg -d po -i msg.pot'],
            'file_dep': ['msg.pot'],
            'targets': ['po/ru_RU.UTF-8/LC_MESSAGES/msg.po'],
           }


def task_mo():
    """Compile translations."""
    return {
            'actions': [
                (create_folder, [f'{PODEST}/ru_RU.UTF-8/LC_MESSAGES']),
                f'pybabel compile -D msg -l ru_RU.UTF-8 -i po/ru_RU.UTF-8/LC_MESSAGES/msg.po -d {PODEST}'
                       ],
            'file_dep': ['po/ru_RU.UTF-8/LC_MESSAGES/msg.po'],
            'targets': [f'{PODEST}/ru_RU.UTF-8/LC_MESSAGES/msg.mo'],
           }


def task_i18n():
    return {
            'actions': None,
            'task_dep': ['pot', 'po', 'mo'],
            'doc': 'task for generating translations',
            }


def task_test():
    pass


def task_html():
    """Make HTML documentationi."""
    return {
            'actions': ['sphinx-build -M html ./docs/source ./TaskTracker/docs/build'],
            'file_dep': glob.glob('docs/source/*.rst') + glob.glob('TaskTracker/*.py'),
            'targets': ['TaskTracker/docs/build'],
            'task_dep': ['i18n'],
            'clean': [(shutil.rmtree, ["TaskTracker/docs/build"])],
           }


def task_style():
    """Check style against flake8."""
    return {
            'actions': ['flake8 TaskTracker/__init__.py', 'flake8 TaskTracker/__main__.py']
           }


def task_docstyle():
    """Check docstrings against pydocstyle."""
    return {
            'actions': ['pydocstyle TaskTracker/__init__.py', 'pydocstyle TaskTracker/__main__.py']
           }


def task_check():
    """Perform all checks."""
    return {
            'actions': None,
            'task_dep': ['style', 'docstyle'] # TODO: + [test']
           }


def task_all():
    """Perform all build task."""
    return {
            'actions': None,
            'task_dep': ['i18n', 'check', 'html'] # TODO + [wheel']
           }


def task_rmdb():
    return {
            'actions': ['rm .*.db'],
            'doc': 'task for removing doit database',
            }


def task_erase():
    return {
            'actions': ['git clean -xdf'],
            'doc': 'task for cleaning uncommited files',
            }


def task_sdist():
    return {
            'actions': ['python -m build -s -n'],
            'task_dep': ['erase', 'rmdb'],
            'doc': 'generate source distribution',
            }


def task_wheel():
    return {
            'actions': ['python -m build -w'],
            'task_dep': ['i18n', 'html'],
            'doc': 'generate wheel',
            }
