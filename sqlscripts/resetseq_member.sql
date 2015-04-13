BEGIN;
SELECT setval(pg_get_serial_sequence('"member_person"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "member_person";
COMMIT;
