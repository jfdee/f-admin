export default [
  {
    path: 'admin',
    name: 'components-admin-view',
    component: () => import ('/components/View.vue'),
    children: [
      {
        path: ':code',
        name: 'components-admin-menu-item-view',
        component: () => import('/components/workspace/View.vue'),
      },
    ],
  },
]
