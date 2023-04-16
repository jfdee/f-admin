import {menuStore} from '/stores/menu'
const _store = menuStore()
export default {
  computed: {
    menuStore() {
      return _store
    },
  },
}