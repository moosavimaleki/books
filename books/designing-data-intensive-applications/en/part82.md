*  Better search—e.g., a search for philanthropists in the state of Washington can match
this profile, because the list of regions can encode the fact that Seattle is in Washington (which
is not apparent from the string "Greater Seattle Area") Whether you store an ID or a text string is a question of duplication. When you use an ID, the
information that is meaningful to humans (such as the word Philanthropy) is stored in only one
place, and everything that refers to it uses an ID (which only has meaning within the database).
When you store the text directly, you are duplicating the human-meaningful information in every
record that uses it. 
The advantage of using an ID is that because it has no meaning to humans, it never needs to change:
the ID can remain the same, even if the information it identifies changes. Anything that is
meaningful to humans may need to change sometime in the future—and if that information is duplicated,
all the redundant copies need to be updated. That incurs write overheads, and risks
inconsistencies (where some copies of the information are updated but others aren’t). Removing such
duplication is the key idea behind normalization in
databases.[ii](ch02.html#idm140605782451264)