# Café Calle Ocho – User Stories and Acceptance Criteria

## 1. Project Overview

Café Calle Ocho is a Flask-based application designed to make ordering food easier for customers and managing orders easier for café staff. Customers can browse the menu, add items to an order, submit orders, and check their order status. Kitchen staff can view incoming orders, update preparation statuses, and manage menu availability.

The goal is to create a simple system that improves communication between customers and café staff while making the ordering process more organized.

## 2. User Personas

### Persona 1: Customer

A customer visits Café Calle Ocho and wants to view the available menu, select food and drinks, submit an order, and know when the order is ready. The customer needs a simple application that is easy to understand and use.

### Persona 2: Kitchen Staff Member

A kitchen staff member is responsible for receiving customer orders, preparing food, and updating order statuses. The staff member needs a clear way to see incoming orders and manage their progress.

## 3. User Stories and Acceptance Criteria

### US-01: Browse the Menu

**As a** customer,  
**I want** to browse the café menu,  
**So that** I can see the available food and drinks before placing an order.

**Priority:** Must Have

**Acceptance Criteria:**

1. Given that the customer opens the menu, when the menu loads, then the application displays available items with their names, descriptions, and prices.
2. Given that a menu category has no available items, when the customer opens that category, then the application displays a message explaining that no items are currently available.

### US-02: Add an Item to an Order

**As a** customer,  
**I want** to add menu items to my order,  
**So that** I can select everything I want to purchase.

**Priority:** Must Have

**Acceptance Criteria:**

1. Given that a menu item is available, when the customer selects the item and adds it to the order, then the item appears in the order with its name, quantity, and price.
2. Given that an item is marked as unavailable, when the customer attempts to add it, then the application prevents the addition and displays an appropriate message.

### US-03: Submit an Order

**As a** customer,  
**I want** to submit my order with my name,  
**So that** the café staff can identify and prepare my order.

**Priority:** Must Have

**Acceptance Criteria:**

1. Given that the customer has at least one available item in the order and has entered their name, when they submit the order, then the application accepts the order and displays an order confirmation with an order number.
2. Given that the order is empty or the customer has not entered a name, when they attempt to submit it, then the application rejects the submission and explains what information is missing.

### US-04: Check Order Status

**As a** customer,  
**I want** to check the status of my order,  
**So that** I know whether my order has been received, is being prepared, or is ready.

**Priority:** Must Have

**Acceptance Criteria:**

1. Given that the customer enters a valid order number, when they check the order status, then the application displays the current status, such as Received, Preparing, Ready, or Picked Up.
2. Given that the customer enters an invalid order number, when they search for the order, then the application displays a message explaining that the order could not be found.

### US-05: View Previous Orders

**As a** customer,  
**I want** to view my previous orders,  
**So that** I can remember what I ordered before.

**Priority:** Could Have

**Acceptance Criteria:**

1. Given that previous orders are associated with the customer's name or contact information, when the customer views their order history, then the application displays the previous orders with their dates and items.
2. Given that the customer has no previous orders, when they open the order history, then the application displays a message explaining that no previous orders are available.

### US-06: View Incoming Orders

**As a** kitchen staff member,  
**I want** to view incoming customer orders,  
**So that** I can see which orders need to be prepared.

**Priority:** Must Have

**Acceptance Criteria:**

1. Given that customers have submitted orders, when the staff member opens the order dashboard, then the application displays active orders with their order numbers, items, quantities, and current statuses.
2. Given that there are no active orders, when the staff member opens the dashboard, then the application displays a message indicating that there are currently no active orders.

### US-07: Update an Order's Preparation Status

**As a** kitchen staff member,  
**I want** to update an order's preparation status,  
**So that** customers can see the progress of their orders.

**Priority:** Must Have

**Acceptance Criteria:**

1. Given that an order has been received, when the staff member changes its status to Preparing, then the application saves the new status and displays the update.
2. Given that an order has already been marked as Picked Up, when the staff member attempts to change it back to Preparing, then the application prevents the invalid update and displays an error message.

### US-08: Mark a Menu Item Unavailable

**As a** kitchen staff member,  
**I want** to mark a menu item as unavailable,  
**So that** customers cannot order food or drinks that are sold out.

**Priority:** Should Have

**Acceptance Criteria:**

1. Given that a menu item is currently available, when the staff member marks it as unavailable, then the application updates the item's availability and shows customers that it is sold out.
2. Given that the staff member attempts to update an item that does not exist, when the update is submitted, then the application displays an error message explaining that the item could not be found.

### US-09: Correct an Order Quantity

**As a** customer,  
**I want** to change the quantity of an item in my order,  
**So that** I can make sure my order contains the correct number of items.

**Priority:** Should Have

**Acceptance Criteria:**

1. Given that an item is already in the customer's order, when the customer enters a valid quantity greater than zero, then the application updates the quantity and recalculates the order total.
2. Given that the customer enters a quantity of zero or a negative number, when they attempt to update the order, then the application rejects the change and asks the customer to enter a quantity of at least one.

## 4. Priority Summary

The user stories are organized by importance to help determine which features should be developed first.

| Priority | User Stories | Description |
|---|---|---|
| Must Have | US-01, US-02, US-03, US-04, US-06, US-07 | Essential features needed for the main ordering process. |
| Should Have | US-08, US-09 | Useful features that improve the application but are not essential for the first version. |
| Could Have | US-05 | An additional feature that can be implemented if time allows. |

## 5. Conclusion

These user stories describe the main functionality of the Café Calle Ocho application from the perspective of both customers and kitchen staff. The acceptance criteria provide specific conditions that can be used to test each feature.

The Must Have stories will be the main focus during the first development stage. The Should Have and Could Have stories can be added after the basic ordering and order management features are working correctly.git add USER_STORIES.md
git commit -m "Add user stories and acceptance criteria"
git push origin main