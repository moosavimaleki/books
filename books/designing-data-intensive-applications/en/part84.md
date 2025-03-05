Moreover, even if the initial version of an application fits well in a join-free document model,
data has a tendency of becoming more interconnected as features are added to applications. For
example, consider some changes we could make to the résumé example: Organizations and schools as entities In the previous description, organization (the company where the user worked) and school_name
(where they studied) are just strings. Perhaps they should be references to entities instead?

Then each organization, school, or university could have its own web page (with logo, news feed,
etc.); each résumé could link to the organizations and schools that it mentions, and include their
logos and other information (see [Figure 2-3](#fig_datamodels_linked_entity) for an example from LinkedIn). Recommendations Say you want to add a new feature: one user can write a recommendation for another user. The
recommendation is shown on the résumé of the user who was recommended, together with the name and
photo of the user making the recommendation. If the recommender updates their photo, any
recommendations they have written need to reflect the new photo. Therefore, the recommendation
should have a reference to the author’s profile.