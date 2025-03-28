import { defineStore } from 'pinia'
import axios from 'axios'

export const menuStore = defineStore('menu', {
  state: () => ({ items: [], selected: null }),
  getters: {
    getSelectedItem(state) {
      if (!state.selected) return
      return state.items.filter(item => item.code === state.selected)[0]
    },
  },
  actions: {
    async init() {
      const {data} = await axios.get('/api/admin/menu/')
      this.items = data
    },
    setSelected(code) {
      this.selected = code
    },
  },
})