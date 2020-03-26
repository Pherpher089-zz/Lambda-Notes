# Research Topics: Potluck Planner
## [Helmet](https://helmetjs.github.io/) 
Helmet helps you secure your Express apps by setting various HTTP headers. *It’s not a silver bullet*, but it can help!

`npm module`

### How it works
Helmet is a collection of 12 smaller middleware functions that set HTTP response headers. Running app.use(helmet()) **will not** include all of these middleware functions by default.

- `contentSecurityPolicy` for setting Content Security Policy
- `dnsPrefetchControl` controls DNS pre-fetching
- `expectCt` for handling Certificate Transparency
- `featurePolicy` to limit your site’s features
- `frameguard` to prevent clickjacking
- `hidePoweredBy` to remove the X-Powered-By header
- `hsts` for HTTP Strict Transport Security
- `ieNoOpen` sets X-Download-Options for IE8+
- `noSniff` to keep clients from sniffing the MIME type
- `permittedCrossDomainPolicies` for handling Adobe products’ crossdomain requests	
- `referrerPolicy` to hide the Referer header
- `xssFilter` adds some small XSS protections	

## [Morgan](https://www.npmjs.com/package/morgan#morganformat-options)
*a reference to Dexter*

`npm module`

HTTP request logger middleware for node.js
```js
//import
var morgan = require('morgan')
```
### morgan(format, options)
Create a new morgan logger middleware function using the given format and options. The format argument may be a string of a predefined name (see below for the names), a string of a format string, or a function that will produce a log entry.

The format function will be called with three arguments tokens, req, and res, where tokens is an object with all defined tokens, req is the HTTP request and res is the HTTP response. The function is expected to return a string that will be the log line, or undefined / null to skip logging.

### Using a predefined format string
```js
morgan('tiny')
```
### Using format string of predefined tokens
```js
morgan(':method :url :status :res[content-length] - :response-time ms')
```
### Using a custom format function
```js
morgan(function (tokens, req, res) {
  return [
    tokens.method(req, res),
    tokens.url(req, res),
    tokens.status(req, res),
    tokens.res(req, res, 'content-length'), '-',
    tokens['response-time'](req, res), 'ms'
  ].join(' ')
})
```
### Options
morgan accepts these properties in the status object
