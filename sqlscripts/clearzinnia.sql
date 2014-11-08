BEGIN;
DROP TABLE "cmsplugin_zinnia_calendarentriesplugin";
DROP TABLE "cmsplugin_zinnia_queryentriesplugin";
DROP TABLE "cmsplugin_zinnia_randomentriesplugin";
DROP TABLE "cmsplugin_zinnia_selectedentriesplugin" CASCADE;
DROP TABLE "cmsplugin_zinnia_selectedentriesplugin_entries" CASCADE;
DROP TABLE "cmsplugin_zinnia_latestentriesplugin" CASCADE;
DROP TABLE "cmsplugin_zinnia_latestentriesplugin_categories" CASCADE;
DROP TABLE "cmsplugin_zinnia_latestentriesplugin_authors" CASCADE;
DROP TABLE "cmsplugin_zinnia_latestentriesplugin_tags" CASCADE;
DROP TABLE "zinnia_category" CASCADE;
DROP TABLE "zinnia_entry" CASCADE;
DROP TABLE "zinnia_entry_categories" CASCADE;
DROP TABLE "zinnia_entry_authors" CASCADE;
DROP TABLE "zinnia_entry_related" CASCADE;
DROP TABLE "zinnia_entry_sites" CASCADE;

COMMIT;
