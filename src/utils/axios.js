import axios from 'axios'
import axiosRetry from 'axios-retry'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axiosRetry(axios, { retries: 3 })
export default axios
