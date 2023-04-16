import { defineStore } from 'pinia'

export const menuStore = defineStore('menu', {
  state: () => ({ items: [], selected: null }),
})