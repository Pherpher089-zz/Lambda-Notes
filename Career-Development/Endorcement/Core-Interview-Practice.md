1. Responsive design concepts
   _Use CSS preprocessors, mixins and built-in functions to create a modern website_ - When designing in a responsive way, the goal is to create a web site that is going to look and function the it was intended on any devise, environment or
   screen size. This requires you to style for several screen sizes using media queries, us responsive units such as `%` or `rem` units and utilizing the `Flex` display property to adjust the position of items according to width of the viewport. Preprocessors are programs that modify input to conform to another programs requirements. The two main preprocessors in use today are Less and Sass. These programs add functionality to standard CSS. These functions include variables, which hold values for things like sizing, color or even font, mixins, which are prepackaged styles that can be inserted into other style scopes and functions, which can perform maths and conditions for styles and values.
2. Accessibility
   _Use HTML tags, CSS selectors, and Flexbox to build a responsive website_ - When making a website accessible, the goal is to design in such a way that the largest amount of people can use the website. This design paradigm follows the universal design theory which states that if you design for the furthest edge case, all other cases will then be satisfied. This would include designing for people with physical disabilities like colorblindness, poor vision or hearing, etc. Also People with poor internet connection or even people with older versions of web browser. For example a large amount of people rely on screen readers to consume written material on sites. In order to make screen readers effective for a site, one must utilize semantic tags, which are tags that use english words.
3. Intro to Javascript
   _Write functions in JavaScript that appropriately use loops and conditionals_ - JavaScript is a functional programming language built in 1994 to give websites more functionality.
4. Applied JS
   PROMISES - Build components to retrieve data from web APIs using abstraction and encapsulation to pass data and callbacks - Promises are special objects that are returned by functions that take some time to execute. It is a promise on data. Once the function is complete, the promise object is updated with the data initially needed by it's returning function. These objects have several states depending on weather or not the original function succeeded or not. Callbacks are functions that are passed into other functions as arguments. A function that has a callback parameter is known as a higher order function.
5. Single Page Apps
   _Use React Router and its components to render nested dynamic routes_ - Single page applications utilize client side routing to render all of tha apps components on a single URL. This prevents the app from refreshing the web page. One of the best ways I know how to do this is with react-router.
6. Single Page Apps
   _Use forms to build interactive Component Behavior_ - The use of Reacts components allows developers to manage form input and create interactive behavior based on that input. By saving the values inputted to the state and then mapping state back onto the input values, we can save and utilize the input provided by users.
7. Redux
   _Use Redux thunks to make statefull API requests with an appropriate spinner UI_ - Redux is a state management library commonly use with react. Redux keeps the applications state in a data store and makes it accessible to the entire application. The only thing that can change the state is an action. Actions create a copy of the existing state and modify it. Once the copy of state has been changed, it then replaces the old state with the new one. A thunk is a middle ware that lets you call action creators that return a function instead of an action object. These functions receive the stores dispatch method and dispatches regular synchronous actions in the body of the function after the asynchronous process has completed. This is especially useful when retrieving data from an API. Once the API call is completed, actions set the stores state with the response from the API. This often done with an axios call.
8. APIs
   _Use RESTful HTTP methods PUT & DELETE to modify data on a server_ - When interfacing with an API, RESTful HTTP methods are used to read, write, modify and delete data on the server. These methods are GET, POST, PUT and DELETE. These methods send a request and receive a response object that contains the data from a successful request, or an error object from one that is not.

9. APIs
   Implement a client-side Login with tokens and protected routes in React

10. Node.js
    Use Express' built-in router to build and test a modular server API with Postman

11. Node.js
    Implement authentication & custom middleware

12. RDBMS
    Use SQL to create and query a local database, table schemas, configure scripted schema migrations & seed scripts
