CREATE SCHEMA "ecommerce";

CREATE TYPE "ecommerce"."products_status" AS ENUM (
  'out_of_stock',
  'in_stock',
  'running_low'
);

CREATE TABLE "ecommerce"."merchants" (
  "id" int,
  "country_code" int,
  "merchant_name" varchar,
  "created at" varchar,
  "admin_id" int,
  PRIMARY KEY ("id", "country_code")
);

CREATE TABLE "ecommerce"."order_items" (
  "order_id" int,
  "product_id" int,
  "quantity" int DEFAULT 1
);

CREATE TABLE "ecommerce"."orders" (
  "id" int PRIMARY KEY,
  "user_id" int UNIQUE NOT NULL,
  "status" varchar,
  "created_at" varchar
);

CREATE TABLE "ecommerce"."products" (
  "id" int PRIMARY KEY,
  "name" varchar,
  "merchant_id" int NOT NULL,
  "price" int,
  "status" ecommerce.products_status,
  "created_at" datetime DEFAULT (now())
);

CREATE TABLE "ecommerce"."product_tags" (
  "id" int PRIMARY KEY,
  "name" varchar
);

CREATE TABLE "ecommerce"."merchant_periods" (
  "id" int PRIMARY KEY,
  "merchant_id" int,
  "country_code" int,
  "start_date" datetime,
  "end_date" datetime
);

CREATE TABLE "users" (
  "id" SERIAL PRIMARY KEY,
  "full_name" varchar,
  "created_at" timestamp,
  "country_code" int
);

CREATE TABLE "countries" (
  "code" int PRIMARY KEY,
  "name" varchar,
  "continent_name" varchar
);

CREATE INDEX "product_status" ON "ecommerce"."products" ("merchant_id", "status");

CREATE UNIQUE INDEX ON "ecommerce"."products" ("id");

COMMENT ON COLUMN "ecommerce"."orders"."created_at" IS 'When order created';

ALTER TABLE "ecommerce"."merchants" ADD FOREIGN KEY ("admin_id") REFERENCES "users" ("id");

ALTER TABLE "ecommerce"."merchants" ADD FOREIGN KEY ("country_code") REFERENCES "countries" ("code");

ALTER TABLE "ecommerce"."order_items" ADD FOREIGN KEY ("order_id") REFERENCES "ecommerce"."orders" ("id");

ALTER TABLE "ecommerce"."order_items" ADD FOREIGN KEY ("product_id") REFERENCES "ecommerce"."products" ("id");

ALTER TABLE "ecommerce"."products" ADD FOREIGN KEY ("merchant_id") REFERENCES "ecommerce"."merchants" ("id");

CREATE TABLE "product_tags_products" (
  "product_tags_id" int NOT NULL,
  "products_id" int NOT NULL,
  PRIMARY KEY ("product_tags_id", "products_id")
);

ALTER TABLE "product_tags_products" ADD FOREIGN KEY ("product_tags_id") REFERENCES "ecommerce"."product_tags" ("id");

ALTER TABLE "product_tags_products" ADD FOREIGN KEY ("products_id") REFERENCES "ecommerce"."products" ("id");


ALTER TABLE "ecommerce"."merchant_periods" ADD FOREIGN KEY ("merchant_id", "country_code") REFERENCES "ecommerce"."merchants" ("id", "country_code");

ALTER TABLE "users" ADD FOREIGN KEY ("country_code") REFERENCES "countries" ("code");
