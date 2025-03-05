These words are often cast around without a clear understanding of what they mean. In the interest
of thoughtful engineering, we will spend the rest of this chapter exploring ways of thinking about
reliability, scalability, and maintainability. Then, in the following chapters, we will look at
various techniques, architectures, and algorithms that are used in order to achieve those goals. # Reliability 
Everybody has an intuitive idea of what it means for something to be reliable or unreliable. For
software, typical expectations include: *  The application performs the function that the user expected. *  It can tolerate the user making mistakes or using the software in unexpected ways. *  Its performance is good enough for the required use case, under the expected load and data volume. *  The system prevents any unauthorized access and abuse. If all those things together mean “working correctly,” then we can understand reliability as
meaning, roughly, “continuing to work correctly, even when things go wrong.”