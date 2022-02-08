CREATE TABLE IF NOT EXISTS "sessions" (
  "session_id" INT NOT NULL,
  "user_id" INT NOT NULL,
  "ip_address" VARCHAR(45) NOT NULL,
  "devices" VARCHAR(45) NOT NULL,
  "OS" VARCHAR(45) NOT NULL,
  "browser" VARCHAR(45) NOT NULL,
  "date_login" TIMESTAMP NOT NULL,
  "date_logout" TIMESTAMP NOT NULL,
  PRIMARY KEY ("session_id"));