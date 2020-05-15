# Web Core Interview

1. Responsive design concepts X
2. Accessibility X
3. JavaScript Fundamentals
4. State management
5. Client-side authentication
6. Client-side Routing
7. Asynchronous patterns
8. Form Management
9. Working with APIs in React
10. Node Express Router
11. Server-side Authentication
12. Database organization

-   Responsive design concepts
    -   Use CSS preprocessors, mixins and built-in functions to create a modern website
-   Accessibility
    -   Use HTML tags, CSS selectors, and Flexbox to build a responsive website
-   Intro to Javascript
    -   Write functions in JavaScript that appropriately use loops and conditionals
-   Applied JS
    -   PROMISES - Build components to retrieve data from web APIs using abstraction and encapsulation to pass data and callbacks
-   Single Page Apps
    -   Use React Router and its components to render nested dynamic routes
-   Single Page Apps
    -   Use forms to build interactive Component Behavior
-   Redux
    -   Use Redux thunks to make stateful API requests with an appropriate spinner UI
-   APIs
    -   Use RESTful HTTP methods PUT & DELETE to modify data on a server
-   APIs
    -   Implement a client-side Login with tokens and protected routes in React
-   Node.js
    -   Use Express' built-in router to build and test a modular server API with Postman
-   Node.js
    -   Implement authentication & custom middleware
-   RDBMS
    -   Use SQL to create and query a local database, table schemas, configure scripted schema migrations & seed scripts

## Responsive design concepts

_Use CSS preprocessors, mixins and built-in functions to create a modern website_

### User Interface Sprint Challenge

-   CSS Reset: A base line style reset for all elements targeted at consistency between web browsers. This overwrites the `User Agent` style sheet which exists to make unstyled sights more readable.
-   myerweb.com has a pretty good one.

### Preprocessor

-   a computer program that modifies data to conform with the input requirements of another program.

**Less.js** and **Sass** are both css preprocessor

#### Mixins

Mixins are like the functions of styling. They are pre-packaged styles that are implemented by reference.

for instance, this is our mixin. Written some where else in the file or in another one all together.

```css
.bordered {
	border-top: dotted 1px black;
	border-bottom: solid 2px black;
}
```

In order to implement this class as a mixin, we just call it like a function

```css
#menu a {
	color: #111;
	.bordered();
}

.post a {
	color: red;
	.bordered();
}
```

### Functions

Functions can transform colors, manipulate strings and do maths. They can also determine an outcome based on a condition.

```css
@some: foo;

div {
	margin: if((2>1) 0, 3);
	color: if(
		(
				iscolor: (
					@some,
				)
			)
			darken(@some, 10%),
		black
	);
}
```

### Responsive design

Responsive Web design is the approach that suggests that design and development should respond to the user’s behavior and environment based on screen size, platform and orientation.

Fixed layout - A style that only works for one platform and screen resolution. The units used for size are usually pixels.
No media queries are used. The only benefit here is faster deployment

Fluid layouts - These expand and contract with the size of the screen. These are cool and all but they can end up acting very wonky and don't always produce the best results. Measurements are usually percentages. No media queries are used.

Adaptive Layouts - Design is often targeted at phones, tabs, and desktops. Layout width are hard coded per media query.

Responsive Layouts - Design is often divided among desktop, tablet, or phone. Responsive units are used throughout the site. Media queries are used. Site accommodates thousands of devices and takes longer to build.

#### Responsive Units

Rems - Root em, this unit bases it relativity of size on the root element of the page. This is usually the `html` tag. Setting the font size to 62.5% in the root element will guarantee that rem units will be 1:10px

Felx-box - A display property that neetly orders a container of tags in a uniform way. The spacing of the elements will adjust to the screen width and height.

media queries - Media queries allow for different css rules based on the width of the viewport. Here is an example of a media query

```css
.container {
	max-width: 800px;
	margin: 0 auto;
	border: 1px solid red;
	padding: 20px 1.25%;
}

@media (max-width: 500px) {
	.container {
		background: gray;
	}

	.container header nav {
		display: flex;
		flex-direction: column;
	}

	.container header nav a {
		margin-bottom: 20px;
	}
}
```

optimal resolutions to design for

W3 Schools suggests targeting these 5 widths: 600px, 768px, 992px, and 1200px. This will cover the mass majority of devices.

```css
/* Extra small devices (phones, 600px and down) */
@media only screen and (max-width: 600px) {
	...;
}

/* Small devices (portrait tablets and large phones, 600px and up) */
@media only screen and (min-width: 600px) {
	...;
}

/* Medium devices (landscape tablets, 768px and up) */
@media only screen and (min-width: 768px) {
	...;
}

/* Large devices (laptops/desktops, 992px and up) */
@media only screen and (min-width: 992px) {
	...;
}

/* Extra large devices (large laptops and desktops, 1200px and up) */
@media only screen and (min-width: 1200px) {
	...;
}
```

Mobile First vs. Desktop first
W3 school recommends always starting with mobile first design. This means start with designing for a small max width first, ie mobile devices and then design for progressively larger widths. This will make web pages load faster on mobile. Desktop first would be the exact opposite of mobile first.

## Accessibility

_Use HTML tags, CSS selectors, and Flex-box to build a responsive website_

What is accessability? Making web pages and the internet accessible to all people, regardless of how they need to interact with the page.

#### Universal design theory

If you design with the furthest out individual in mind will end up benefiting all individuals who use the product. Ie. installing wheel chair ramps on sidewalks helps people with carts or strollers as well.

One of the most simple yet effective ways to make a web page accessible is to use responsive units.

**Screen readers** are tools used to read the screen for those with visual impairments. In order to make this useful, one must design using semantic tags such as `h1`, `article` or `p`. These are the tags resembling english. This is due to the nature of the screen reader. It begins with the `h1` element and continues to read sub elements as it sees appropriate. Things like `div`s and `span`s do not give any definition to its content.

Other tips include using meaningful class names and ids on elements and always give your images alt text

**Color** is another big issue. If one is using color to convey important information such as an input field turning red to inform the user of invalid input, one may want to include some kind of icon to convey that same message to those who cant see color correctly

## Intro to Javascript

_Write functions in JavaScript that appropriately use loops and conditionals_

The third and final building block of a web page. Developed in 1994 to give websites more functionality. I know ES6. Though it has OOP properties, it is not a true OOP language.

**Variables**

-   let - code block scope - mutable
-   var - global scope - mutable
-   const - global scope - immutable

**Data types**

-   number - any data consisting of a number or numeric value
-   string - Data containing letters of the alphabet. Always incased in quotes
-   bool - Data that is either true or false.
-   null/undefined - These data types represent variables with no lagitemit data. If a variable is declared and not defined, the code will return `undefined`. The computer will return `null` in the same case however, a developer must set the value to `null`, meaning it has no value yet.

## State Management

The state of an application is a top level data store for the whole application. The advantage is that all of the components in the application can access this state. There are a few different ways we can do this. One would be to used Redux. Redux is a state management lib that works along side React as well as other frameworks. Redux can be cumbersome and so our other option for state management is to use Reacts new built in functionality Hooks and Context API.

### Redux

Redux is a state management library commonly used along side React. Redux is built on the principal of immutability. This is more or less a safety feature to prevent bugs because mutations are hidden and can be hard to see. In order to manage the redux store, one has to dispatch actions.

The core concepts/principals for Redux are:

**The Store** - Everything that changes within your JS application is represented by a JS object called the `store`. We never mutate the original object and we never write to our store object.

**Application state is Immutable** - We never mutate the state. We create a clone of the state object, make the changes to it and replace the original state with the new object. We never write to our state object.

**Pure functions change our state** - Givin the same input, a pure function will return the same thing every time. All functions(reducers) in Redux must be pure.

**What is a reducer?**

A reducer is a function that determines changes to the state. It uses the action it receives to determine this change. Reducers take state and an action and create a new state based on these two parameters.

**What is an action?**
Actions are the only source of information for store. It carries a payload of information from your application to the store. These are plain js objects that have a type attribute.

### Context

The context API is tool for managing and distributing state globally throughout your application. The parent element is wrapped in the context component and passed in a value. This component is called the provider. Any child component to the provider can tap into the context state with the consumer component.

### Hooks

Hooks are a way of adding state to functional components. This makes the code more light weight and readable.

## Client-side authentication

In order for a client to gain authentication, it must send the server a correct set of credentials and the server will send back a JWT or `Jason Web Token` That verifies authentication. This token is stored in `localStorage` or `sessionStorage`

A common pattern is for a login endpoint to exist which takes a payload of username and password and responds with a JWT. The server must then pass that token back to the server in the header of ever request from then on, under a key like `Authorization`. This will allow access to protected portions of the server.

Once the client has the token stored, two layers of authentication can be added. The first is mentioned above where the client sends the token in the header of the request. The other is to create a protected route that will only render if the auth token exists. If it does not, it redirects to a public portion of the website.

Another and older solution to this would be for the server to store a cookie on each client.

### JWT

Jason Web Tokens are strings of hashed JSON data. These tokens have three parts separated by periods. For example:

> `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`

The first portion of this string of unintelligible text is the `Header`

> `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9`

The header is a hashed JS object with two fields. The
algorithm and token type:

```JSON
{
	"alg": "HS256",
	"typ": "JWT"
}
```

This particular algorithm is the HMAC-SHA256 algorithm. This is the algorithm that will encrypt the JSON object.This portion of the token is then encoded.

The second Portion is the `Payload` and it and contains all of the actual useful Data from the token. This data is known as the claims. These are claims about the entity(typically the user). This portion of the token is then encoded.

#### Registered claims

These are a set of predefined claims that are not required but recommend. some of them are: iss (issuer), exp (expiration time), sub (subject), aud (audience), and others

#### Public claims

These can be defined at will by those using JWTs. But to avoid collisions they should be defined in the IANA JSON Web Token Registry or be defined as a URI that contains a collision resistant namespace.

#### Private claims

These are the custom claims created to share information between parties that agree on using them and are neither registered or public claims.

```JSON
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
```

> Do note that for signed tokens this information, though protected against tampering, is readable by anyone. Do not put secret information in the payload or header elements of a JWT unless it is encrypted.

The third and final portion of the token is the `Signature`. This portion takes the encoded header, the encoded payload and a `secret` which is a unique string that is used as salt on the hashing algorithm to enure is uniqueness and is all hashed. Note that this is the only portion of the token that can not be read by the public or any one without the secret for that matter.

```JSON
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)
```

## Client-side routing

All web sites and applications use routing. This is discovering parts of the sight by changing the URL. Weather an application has client side or server side routing, it is still accessed from a server. How a website or app responds to different URL's is commonly handles server side but emerging JS libs, other ways of routing have been discovered.

Routing is the mechanism by which requests are connected to some code. It is essentially the way you navigate through a website or web-application. By clicking on a link, the URL changes which provides the user with some new data or a new webpage.

### Server Side

When a link is clicked and the route is changed, the server sends an entirely new document, and discards the previous. This causes the whole page to refresh.

#### Pros

-   With server side routing, only the data that is needed is sent to the client. No more, no less.
-   Because this is the standard for such a long time, search engines are optimized for webpages that come from the server.

#### Cons

-   The client may request redundant data. Refreshing the whole page when the nav bar and footer are the same as the last page
-   Can take a while for the page to render. This is only typical if the document is irregularly large or internet speed is slow.

### Client Side

A client side route happens when the route is handled by
the java script that is loaded on the web page. The adjustment to the URL will result in a changed state of the application.

It is important to note that the whole page won’t refresh when using client-side routing. There are just some elements inside the application that will change.

#### Pros

-   Because less data is processed, it is much quicker.
-   Smooth transitions and animation between views are much easier to implement.

#### Cons

-   The whole website or web-application needs to be loaded on the first request. That’s why the initial loading time usually takes longer.
-   Because the whole website or web-application is loaded initially, there is a possibility that there is data downloaded for views you won’t even come across.
-   It requires more setup work or even a library. Because server-side is the standard, extra code must be written to make client-side routing possible.
-   Search engine crawling is less optimised. Google is making good progress on crawling single-paged-apps, but it isn’t nearly as efficient as server-side routed websites.

### React Router

Client side routing in React is done through the `react-router-dom` package. With this package, we can render components based on the URL. This is done with the `Route` component. Note that the parent `App` component must be wrapped in a `Router` component.

```JavaScript
mport React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

export default function App() {
  return (
    <Router>
      <div>
		{/* rest of the app*/}
      </div>
    </Router>
  );
}
```

In order to assign component to different routes, we have to set up route components.

```JS
export default function App() {
  return (
    <Router>
      <div>
		<Route path="/about">
			<ComponentToRender />
		<Route/>
		<Route path="/contact">
			<ComponentToRender />
		<Route/>
		<Route path="/portfolio">
			<ComponentToRender />
		<Route/>
      </div>
    </Router>
  );
}
```

The child component of these routes will render if the "path" is added to the end of the URL. In order for the user to change the URL, we have to set up some links. Links are interactive elements that will change the URL when clicked on.

```JS
export default function App() {
  return (
    <Router>
      <div>
	  <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/users">Users</Link>
            </li>
          </ul>
        </nav>

		<Route path="/about">
			<ComponentToRender />
		<Route/>
		<Route path="/contact">
			<ComponentToRender />
		<Route/>
		<Route path="/portfolio">
			<ComponentToRender />
		<Route/>
      </div>
    </Router>
  );
}
```

## Asynchronous patterns

JavaScript is an singly threaded language.

### callbacks

In javascript a function that takes a function as an argument is considered to be a higher order function. While Call backs them selves are not asynchronous, this kind of function is key to asynchrony.

### promises

A promise is an object that is created while waiting for an asynchronous process to end. Once that process ends, it will send its data to that promise object. The promise object has three states, pending, fulfilled or rejected. Once the asynchronous process is started, the promise object is returned by the function running that process and its status is set to unresolved. Once that process is resolved, the promise objects status is set to resolved and the value is set if it is returned by the process.

### async/await

async/await is an ES6 functionality.

The `async` key word is placed before a function declaration and causes that function to return a promise. If the value that this function is returning is not a promise, it is wrapped in one. Meaning that a promise is returned with the value being what the function returned. For example.

```JavaScript
async function () {
	return 1
}
```

This function will return a promise with the value set to 1.

The `await` key word is placed before a process that may take some time and will cause the execution of the async function to pause until the value of the process is returned, then returns the resolved promise.

```JavaScript
async function () {
	let promise = new Promise((resolve, reject) => {
		setTimeOut(()=>{
			resolve("done"), 1000
		})
		let result = await promise;
		alert(result);
	})
}

f();
```

This function will begin and pause at the line that assigns result to promise. Notice the `await` key word. This assignment will only complete after promise is resolved and then result will be assigned that promise.

## Form Management

Forms are a collection of input types presented to the user on a web page with a goal of collecting data. In React, it is common to collect input from these forms and assign them to state variables. When submitted, that state variable is usualy sent to a `post` api call through a hook or action if Redux is in use.

```JS
class Component extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			input:"",
		}
	}

	render() {
		<form>
			<input name="input" placeHolder="Your input here" value={this.state.input} onChange={(e)=>{
				this.setState({
					input:e.target.value
				})
			}}/>
		</form>
	}
}
```

This will take what the user types into the input field and set the state accordingly while at the same time, assigning the value of the input to the state.

#### Client Side Form Validation

Client side validation is the process of insuring that the input is valid and in the correct format before submitting the data to the server. If the user does not enter a valid user name or a username at all, the form validation should prevent it from being sent to the server and alert the user of the mistake.

#### Different types of client-side validation

There are two different types of client-side validation that you'll encounter on the web:

-   Built-in form validation uses HTML5 form validation features, which we've discussed in many places throughout this module. This validation generally doesn't require much JavaScript. Built-in form validation has better performance than JavaScript, but it is not as customizable as JavaScript validation.
-   JavaScript validation is coded using JavaScript. This validation is completely customizable, but you need to create it all (or use a library).

## Working with APIs in React

> Use RESTful HTTP methods PUT & DELETE to modify data on a server

`Axios` is the HTTP client that I know. Axios allows for a JS client to make requests to an API.

These requests are made through the HTTP protocol and we use the acronym CRUD to remember the actions that can be taken through this protocol.

-   C - Create
-   R - Read
-   U - Update
-   D - Delete

All HTTP request methods need at least one argument, which is the URL to the server. Different versions of that URL get different results from the server. For instance. `https://my-server.com/user` might be the url used to retrieve, create or modify user data. The type of action that is performed along with this route depends on the HTTP request method that is being used.

We use the HTTP request method `POST` to create data. This method usually has data in its body that is being sent to be created on the db.

We use the HTTP method `GET` to read data from the server. This method doesn't require a body.

We use the HTTP method `PUT` to modify existing data on the db. This requires the changes that are to be made to be sent in the body of the request.

We use the HTTP method `DELETE` to remove data from the database. _note: when using axios, this method requires the id of the record to be deleted to be placed in the URL as a parameter_

## Node Express Router

> Use Express' built-in router to build and test a modular server API with Postman

Nodes Express is an un-opinionated web API for node. The Router feature of express allows for creating robust routes on your server. These routes assign HTTP request methods to specific request handlers on your server. These methods have two arguments. The first is the requirements and the second is the result. These are abbreviated as `req` and `res`.

Requirements or the `req` are the payload from the request sent by the client. These have a header and body component. This data is used within the routes callback in what ever operation its performing.

Results or the `res` is what is returned to the client after the callback has retrieved or created data on the db. Two important methods of the `res` object are `.status()` and `.json()`

The `.status()` takes a numeric argument usually between 100 and 500 and represents the outcome of the request determined by the server.

Another way of sending data to a request handler is via `route parameters`. Route parameters variable portions of the route that can be used in the request.

    `https://my-server.com/user/:id`

For instance in this route `/user/:id`, id is a reference to an id sent from the client. In this case, it's probably the id of the users record in the db.

Another method for sending information to the server that is similar to a route parameter is a `string query`. There can be multiple string queries within a route and are represented by key value pairs. For example:

    `https://my-server.com/user?username=chris&userId=13`

These string queries are added to the req.query object and do not need to be specified by the route. Because they are not defined by the route on the route handler, it's good practice to create a default condition if none are passed in via the route.

## Server-side Authentication

**Authentication** is the process by which our Web API verifies the identity of a client that is trying to access a resource. This is different from **authorization**, which comes after authentication and determines what type of access, if any, that a user should have.

-   Encryption goes two ways. First, it utilizes plain text and private keys to generate encrypted passwords and then reverses the process to match to an original password.
-   Cryptographic hashes only go one way: parameters + input = hash. It is pure; given the same parameters and input it generates the same hash.

If the database of users and keys are compromised, it is possible to decrypt the passwords to their original values, and this is bad because users often share passwords across different sites. This is one reason why `cryptographic hashing is the preferred` method for storing user passwords.

### Middleware

Authentication on the server is often handled via a middleware. Middle ware is functionality that is added to a route and is executed before the route handlers code. This is functionality that is layered into the route. For authentications sake, the client will send a JWT in the header of the request. All routes that are protected will have a protected middle ware to validate this toke before the server ever gets to the code in the route handler. If the token is invalid, the execution of the handler will stop and the request will be rejected. It's important to note that a middle takes in the same parameters as the route handler along with a parameter called next. This allows for the middleware to pass the request off to its handler when the `next()` method is called.

### Validating a JWT

In order to verify a JWT, we need a `secret`. This string will be used to unhash the JWT. This is done via a method on the `jwt` object that must be imported from the jsonwebtoken package. This method takes three arguments. The token, the secret and the callback that handles what happens if the token is valid and if it is not.

## Database organization

A database is **a collection of data organized for easy retrieval and manipulation**. Relational databases are dbs that store related data. These are the oldest and most common databases in use today.

Databases are most necessary due to the need of data persistance. Persistent data is data that is stored safely and is unlikely to change.

In relational databases, the data is stored in tabular format grouped into rows and columns (similar to spreadsheets). A collection of rows is called a table. Each row represents a single record in the table and is made up of one or more columns.

### Schema

Database schema is the structure of data described by a formal language supported by the DBMS(Data Base Management System - Knex is what I know). The term schema is a reference to the organization of the data as a blueprint.

### Normalization

Normalized dbs have data that does not overlap or repeat its self. Every table in a normalized db contains data for a specific topic.

1.  contains no repeating groups of data
2.  Only Data that relates to it's primary key is stored in said table
3.  There are no in-table dependencies between the columns in each table

These are considered to be the three levels of normalization for data

> Check your written notes
