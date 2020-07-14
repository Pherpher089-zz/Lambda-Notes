# Research Topics: Potluck Planner

## [Helmet](https://helmetjs.github.io/)

Helmet helps you secure your Express apps by setting various HTTP headers. _It’s not a silver bullet_, but it can help!

`npm module`

### How it works

Helmet is a collection of 12 smaller middleware functions that set HTTP response headers. Running app.use(helmet()) **will not** include all of these middleware functions by default.

-   `contentSecurityPolicy` for setting Content Security Policy
-   `dnsPrefetchControl` controls DNS pre-fetching
-   `expectCt` for handling Certificate Transparency
-   `featurePolicy` to limit your site’s features
-   `frameguard` to prevent clickjacking
-   `hidePoweredBy` to remove the X-Powered-By header
-   `hsts` for HTTP Strict Transport Security
-   `ieNoOpen` sets X-Download-Options for IE8+
-   `noSniff` to keep clients from sniffing the MIME type
-   `permittedCrossDomainPolicies` for handling Adobe products’ crossdomain requests
-   `referrerPolicy` to hide the Referer header
-   `xssFilter` adds some small XSS protections

## [Morgan](https://www.npmjs.com/package/morgan#morganformat-options)

_a reference to Dexter_

`npm module`

HTTP request logger middleware for node.js

```js
//import
var morgan = require("morgan");
```

### morgan(format, options)

Create a new morgan logger middleware function using the given format and options. The format argument may be a string of a predefined name (see below for the names), a string of a format string, or a function that will produce a log entry.

The format function will be called with three arguments tokens, req, and res, where tokens is an object with all defined tokens, req is the HTTP request and res is the HTTP response. The function is expected to return a string that will be the log line, or undefined / null to skip logging.

### Using a predefined format string

```js
morgan("tiny");
```

### Using format string of predefined tokens

```js
morgan(":method :url :status :res[content-length] - :response-time ms");
```

### Using a custom format function

```js
morgan(function (tokens, req, res) {
	return [
		tokens.method(req, res),
		tokens.url(req, res),
		tokens.status(req, res),
		tokens.res(req, res, "content-length"),
		"-",
		tokens["response-time"](req, res),
		"ms",
	].join(" ");
});
```

### Options

morgan accepts these properties in the status object.

-   `immediate`
    Write log line on request instead of response. This means that a request will be logged even if the server crashes, _but data from the responcse(like the response code, content lnegth, ect) can not be logged._

-   `skip`
    function to determine if logging is skipped, defaults to `false`. This function will be called as `skip(req, res)`.

```js
// EXAMPLE: only log error responses
morgan("combined", {
	skip: function (req, res) {
		return res.statusCode < 400;
	},
});
```

-   `stream`
    Outputs streem for writting log lines, defaults to `process.stdout`.

### Predefined Formats

There are various pre-defined formats provided:

-   `combined`
    standard Apache combined log output.

### Redux Thunk

Redux Thunk middleware allows you to write actions that return a function instead of an action. The thunk can be used to delay the dispatch of an action, or to dispatch only if a certain condition is met. The inner function receives the store methods `dispatch` and `getState` as parameters

An action creator that returns a function to perform asynchronous dispatch:

```js
const INCREMENT_COUNTER = "INCREMENT_COUNTER";

function increment() {
	return {
		type: INCREMENT_COUNTER,
	};
}

function incrementAsync() {
	return (dispatch) => {
		setTimeout(() => {
			// Yay! Can invoke sync or async actions with `dispatch`
			dispatch(increment());
		}, 1000);
	};
}
```

An action creator that returns a function to perform conditional dispatch:

```js
function incrementIfOdd() {
	return (dispatch, getState) => {
		const { counter } = getState();

		if (counter % 2 === 0) {
			return;
		}

		dispatch(increment());
	};
}
```

**What is a thunk?!**
A `thunk` is a function that wraps an expression to delay it's evaluation.

```js
// calculation of 1 + 2 is immediate
// x === 3
let x = 1 + 2;

// calculation of 1 + 2 is delayed
// foo can be called later to perform the calculation
// foo is a thunk!
let foo = () => 1 + 2;
```

The term originated as a humorous past-tense version of "think".

**Composition**
Any return value from the inner function will be available as the return value of dispatch itself. This is convenient for orchestrating an asynchronous control flow with thunk action creators dispatching each other and returning Promises to wait for each other’s completion:

```js
import { createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import rootReducer from "./reducers";

// Note: this API requires redux@>=3.1.0
const store = createStore(rootReducer, applyMiddleware(thunk));

function fetchSecretSauce() {
	return fetch("https://www.google.com/search?q=secret+sauce");
}

// These are the normal action creators you have seen so far.
// The actions they return can be dispatched without any middleware.
// However, they only express “facts” and not the “async flow”.

function makeASandwich(forPerson, secretSauce) {
	return {
		type: "MAKE_SANDWICH",
		forPerson,
		secretSauce,
	};
}

function apologize(fromPerson, toPerson, error) {
	return {
		type: "APOLOGIZE",
		fromPerson,
		toPerson,
		error,
	};
}

function withdrawMoney(amount) {
	return {
		type: "WITHDRAW",
		amount,
	};
}

// Even without middleware, you can dispatch an action:
store.dispatch(withdrawMoney(100));

// But what do you do when you need to start an asynchronous action,
// such as an API call, or a router transition?

// Meet thunks.
// A thunk is a function that returns a function.
// This is a thunk.

function makeASandwichWithSecretSauce(forPerson) {
	// Invert control!
	// Return a function that accepts `dispatch` so we can dispatch later.
	// Thunk middleware knows how to turn thunk async actions into actions.

	return function (dispatch) {
		return fetchSecretSauce().then(
			(sauce) => dispatch(makeASandwich(forPerson, sauce)),
			(error) =>
				dispatch(apologize("The Sandwich Shop", forPerson, error))
		);
	};
}

// Thunk middleware lets me dispatch thunk async actions
// as if they were actions!

store.dispatch(makeASandwichWithSecretSauce("Me"));

// It even takes care to return the thunk’s return value
// from the dispatch, so I can chain Promises as long as I return them.

store.dispatch(makeASandwichWithSecretSauce("My wife")).then(() => {
	console.log("Done!");
});

// In fact I can write action creators that dispatch
// actions and async actions from other action creators,
// and I can build my control flow with Promises.

function makeSandwichesForEverybody() {
	return function (dispatch, getState) {
		if (!getState().sandwiches.isShopOpen) {
			// You don’t have to return Promises, but it’s a handy convention
			// so the caller can always call .then() on async dispatch result.

			return Promise.resolve();
		}

		// We can dispatch both plain object actions and other thunks,
		// which lets us compose the asynchronous actions in a single flow.

		return dispatch(makeASandwichWithSecretSauce("My Grandma"))
			.then(() =>
				Promise.all([
					dispatch(makeASandwichWithSecretSauce("Me")),
					dispatch(makeASandwichWithSecretSauce("My wife")),
				])
			)
			.then(() => dispatch(makeASandwichWithSecretSauce("Our kids")))
			.then(() =>
				dispatch(
					getState().myMoney > 42
						? withdrawMoney(42)
						: apologize("Me", "The Sandwich Shop")
				)
			);
	};
}

// This is very useful for server side rendering, because I can wait
// until data is available, then synchronously render the app.

store
	.dispatch(makeSandwichesForEverybody())
	.then(() =>
		response.send(ReactDOMServer.renderToString(<MyApp store={store} />))
	);

// I can also dispatch a thunk async action from a component
// any time its props change to load the missing data.

import { connect } from "react-redux";
import { Component } from "react";

class SandwichShop extends Component {
	componentDidMount() {
		this.props.dispatch(makeASandwichWithSecretSauce(this.props.forPerson));
	}

	componentDidUpdate(prevProps) {
		if (prevProps.forPerson !== this.props.forPerson) {
			this.props.dispatch(
				makeASandwichWithSecretSauce(this.props.forPerson)
			);
		}
	}

	render() {
		return <p>{this.props.sandwiches.join("mustard")}</p>;
	}
}

export default connect((state) => ({
	sandwiches: state.sandwiches,
}))(SandwichShop);
```

**Injecting a Custom Argument
**
Since 2.1.0, Redux Thunk supports injecting a custom argument using the `withExtraArgument` function:

```js
const store = createStore(
	reducer,
	applyMiddleware(thunk.withExtraArgument(api))
);

// later
function fetchUser(id) {
	return (dispatch, getState, api) => {
		// you can use api here
	};
}
```

To pass multiple things, just wrap them in a single object and use destructuring:

```js
const store = createStore(
  reducer,
  applyMiddleware(thunk.withExtraArgument({ api, whatever }))
)

// later
function fetchUser(id) {
  return (dispatch, getState, { api, whatever }) => {
    // you can use api and something else here
  }
}`
```
