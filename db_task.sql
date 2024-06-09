CREATE TABLE "task_info" (
  "task_id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "task_name" varchar(255),
  "task_supervisor" integer,
  "task_workers" integer[],
  "percent" integer
);

CREATE TABLE "task_entry" (
  "entry_id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "task_id" integer,
  "workers_id" integer,
  "entry_description" varchar(255),
  "percent" integer,
  "date" timestamp
);

ALTER TABLE "task_entry" ADD FOREIGN KEY ("task_id") REFERENCES "task_info" ("task_id");
