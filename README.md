# largest-prime-factor
A simple web server that returns the largest prime factor of a given number.

<br>
## How to Use
### 1. Use Ainized Build (EASY)
#### Run on Ainize
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/htcrefactor/largest-prime-factor)

#### Public Address
`https://master-largest-prime-factor-htcrefactor.endpoint.ainize.ai/?number=${YOUR_NUMBER}`

<br>
### 2. Manual Build (DIFFICULT)
#### Docker Build
`docker build -t largest-prime-factor .`

#### Docker Run
`docker run -d -p 80:80 largest-prime-factor`

#### Querying Server
`http://localhost:80/?number=${YOUR_NUMBER}`

<br>
## References
- [Ainize-Team : Primality Test Example](https://github.com/ainize-team/ainize-run-primality-test-example)
