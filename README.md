# CRUD With REST API

This assignment involves creating a CRUD (Create, Read, Update, Delete) application using Django Rest Framework. Below are the instructions to follow:

## Instructions

1. **Create a new app**: Start by creating a new Django app for the project.

2. **Use the Django Rest Framework**: Utilize the Django Rest Framework to build the RESTful API.

3. **Create a product model**: Define a model for products with fields such as `name`, `price`, `inventory` (integer), and `category`.

4. **Create a category model**: Implement a model for categories and establish a link between the category and product models.

5. **Create views**:
   - Create endpoint: Develop an endpoint to create new products.
   - Detailed info endpoint: Design an endpoint to retrieve detailed information about a specific product.
   - Product listing: Implement an endpoint to list all products.
   - Endpoint to delete the product: Create an endpoint to delete a product.
   - Change endpoint (update): Implement an endpoint to update a product, allowing only changes to the stock (inventory).

6. **View Details**:
   - Display name and price in the product listing.
   - Provide detailed information about each product.

7. **Deletion**:
   - Implement deletion functionality using the HTTP DELETE method. The endpoint should receive the object ID and delete the corresponding product based on this ID.

8. **Update**:
   - During the update process, only the stock (inventory) of a product should be allowed to be changed. Use the appropriate serializer to achieve this.

## Submission

- Work independently on the assignment.
- Provide a link to the Git repository containing your project code.

Ensure that you adhere to the guidelines mentioned above to successfully complete the CRUD application with REST API using Django Rest Framework.
