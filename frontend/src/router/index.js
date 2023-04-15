import { createRouter, createWebHistory } from 'vue-router'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'root',
      redirect: r => ({name: 'components-admin-view', params: r.params}),
      // TODO: отдельным роутером
      children: [
        {
          path: 'admin',
          name: 'components-admin-view',
          component: () => import ('/components/admin/View.vue'),
          children: [
            {
              path: ':code/',
              name: 'components-admin-menu-item-view',
              props: r => ({code: r.params.code}),
              component: () => import('/components/admin/MenuItemView.vue'),
            },
          ],
        },
      ]
    },
  ]
})

export default router
