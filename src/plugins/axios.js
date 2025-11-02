import axios from 'axios'

const ajax = axios.create({
  // baseURL: import.meta.env.VITE_SERVER_HOST,
  baseURL: 'http://localhost:8000',
})

export default {
  install: (app) => {
    app.config.globalProperties.$ajax = ajax
  }
}