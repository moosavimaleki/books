What about backward compatibility? As long as each field has a unique tag number, new code can
always read old data, because the tag numbers still have the same meaning. The only detail is that
if you add a new field, you cannot make it required. If you were to add a field and make it
required, that check would fail if new code read data written by old code, because the old code will
not have written the new field that you added. Therefore, to maintain backward compatibility, every
field you add after the initial deployment of the schema must be optional or have a default value. Removing a field is just like adding a field, with backward and forward compatibility concerns
reversed. That means you can only remove a field that is optional (a required field can never be
removed), and you can never use the same tag number again (because you may still have data written
somewhere that includes the old tag number, and that field must be ignored by new code).