The Datalog approach requires a different kind of thinking to the other query languages discussed in
this chapter, but it’s a very powerful approach, because rules can be combined and reused in
different queries. It’s less convenient for simple one-off queries, but it can cope better if your
data is complex. # Summary Data models are a huge subject, and in this chapter we have taken a quick look at a broad variety of
different models. We didn’t have space to go into all the details of each model, but hopefully the
overview has been enough to whet your appetite to find out more about the model that best fits your
application’s requirements. Historically, data started out being represented as one big tree (the hierarchical model), but that
wasn’t good for representing many-to-many relationships, so the relational model was invented to
solve that problem. More recently, developers found that some applications don’t fit well in the
relational model either. New nonrelational “NoSQL” datastores have diverged in two main
directions: