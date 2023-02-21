#!/usr/bin/env python
# coding: utf-8

# # Assignment_18-02-2023

# ## 1. What is an API? Give an example, where an API is used in real life.
# 
# ### Ans:-
#             An API, or(Application Programming Interface), is a set of protocols, routines, and tools for building software
#             applications. It defines how software components should interact and communicate with each other, allowing 
#             developers to create applications that can easily integrate with other software systems.
#             
#                                             An example of an API used in real life is the Google Maps API, which allows
#             developers to integrate Google Maps into their own applications. With this API, developers can access various
#             features of Google Maps, such as location data, routing information, and real-time traffic updates, and use 
#             them to build custom applications for their users. This API is widely used in a variety of industries, 
#             including transportation, logistics, and tourism, to help users navigate their surroundings and find the 
#             information they need.
# 
# 

# ## 2. Give advantages and disadvantages of using API.
# 
# ### Ans:-
# 
#             Advantages of using API:-------->
#             
#             1.Reusability:- APIs can be reused across different applications, allowing developers to save time and resources 
#             by not having to create the same functionality from scratch for each project.
#             
#             2.Scalability:- APIs can handle large amounts of data and traffic, making them ideal for applications that 
#             require high levels of scalability and performance.
#             
#             3.Interoperability:- APIs allow different systems to communicate with each other, even if they are built on 
#             different technologies or platforms, making it easier to integrate systems and share data.
#             
#             4.Flexibility:- APIs can be customized to meet the specific needs of different applications and users, providing
#             greater flexibility and versatility in software development.
# 
#            
#            
#            Disadvantages of using API:------------------>
#            
#            1.Dependency:- Applications that use APIs are often dependent on the functionality and availability of the API
#            provider. If the provider experiences downtime or makes changes to the API, it can cause issues for the 
#            applications that rely on it.
#            
#            2.Security:- APIs can potentially expose sensitive data to unauthorized users if they are not properly secured 
#            and authenticated.
#            
#            3.Complexity:- APIs can be complex to implement and maintain, requiring a significant amount of time and 
#            resources to ensure they are functioning properly and meeting the needs of users.
#            
#            4.Cost:- Some APIs require a fee for access, which can be a significant expense for developers or businesses that
#            rely on them. Additionally, integrating and maintaining an API can also require additional costs for development 
#            and testing.
# 
# 

# ## 3.What is a Web API ? Differentiate between API and Web API?
# 
# ### Ans:-
# 
#           A Web API, or (Web Application Programming Interface), is an API that is designed specifically for web
#           applications. It is a set of protocols and tools for building web-based software applications that can 
#           interact with other software systems or services over the internet.
#           
#           The main difference between an API and a Web API is that a Web API is designed specifically for web applications,
#           while an API can be used for any type of software application. Web APIs are typically designed to be accessed 
#           through HTTP requests and responses, and they often use standard web technologies like JSON, XML, and RESTful web
#           services.
#           
#                                           Another key difference between API and Web API is that Web APIs are often 
#           publicly available and accessible over the internet, while APIs may be more commonly used within closed systems 
#           or for private integrations.
# 
#     In summary, while both APIs and Web APIs serve the same purpose of allowing software applications to interact with each 
#     other, a Web API is specifically designed for web-based applications, uses web technologies, and is often publicly 
#     accessible over the internet.
# 
# 

# ## 4. Explain REST and SOAP Architecture. Mention shortcoming of SOAP.
# 
# ### Ans:-
# 
#             REST (Representational State Transfer) and SOAP (Simple Object Access Protocol) are two different architectures 
#             used for designing web services.
#             
# REST Architecture:----------->
#             
#             REST is an architectural style that defines a set of constraints and principles for designing web services. 
#             It is based on the HTTP protocol and uses standard HTTP methods such as GET, POST, PUT, and DELETE to perform
#             operations on resources. RESTful web services use URLs to represent resources and use standard data formats like
#             JSON and XML for data exchange.RESTful services are often lightweight, easy to implement, and scalable. They 
#             also provide better performance compared to SOAP-based services due to the lack of additional overhead from 
#             the SOAP protocol.
# 
# 
# SOAP Architecture:-------------->
# 
#            SOAP is a protocol-based architecture that uses XML for data exchange and communication between applications. 
#            It defines a standard message format and a set of rules for exchanging messages between applications over a 
#            network. SOAP services are often more secure and reliable than RESTful services because they use a standardized
#            format for communication and support more complex messaging patterns. However, they can also be more complex and
#            slower than RESTful services due to the additional overhead from the SOAP protocol.
#            
# Shortcomings of SOAP:------------>
# 
#            1.Complexity:- The SOAP protocol is often complex and can be difficult to implement and maintain, especially for
#            simple applications.
#            
#            2.Performance:- The additional overhead from the SOAP protocol can cause slower performance compared to RESTful
#            services.
#            
#            3.Limited language support:- SOAP services are typically designed to work with specific programming languages, 
#            making them less flexible and adaptable than RESTful services.
#            
#            4.Scalability:- SOAP services can be less scalable than RESTful services due to the additional overhead and 
#            complexity of the protocol.
# 
# 

# ## 5 . Differentiate between REST and SOAP.
# 
# ### Ans:-
# 
#                  SOAP API                                                            REST API
#  ______________________________________________________________________________________________________________________________                
#       1.Relies on SOAP (Simple Object Access Protocol)                 1.Relies on REST (Representational State Transfer) 
#                                                                           architecture using HTTP.
#                                                                        2.Generally transports data in JSON. It is based on 
#       2.Transports data in standard XML format.                          URL.Because REST follows stateless model, 
#                                                                          REST does not enforces message format as XML       
#       3.Because it is XML based and relies on SOAP,                      or JSON etc.
#         it works with WSDL                                             3. It works with GET, POST, PUT, DELETE
#       4.Highly structured/typedGenerally transports data in JSON.      4. Works over HTTP and HTTPS.
#       5.Designed with large enterprise applications in mind            5. Designed with mobile devices in mind.
# 
