export default [
  {
    path: 'admin',
    name: 'components-admin-view',
    component: () => import ('./View.vue'),
    children: [
      {
        path: ':code',
        name: 'components-admin-menu-item-view',
        component: () => import('./workspace/View.vue'),
      },
    ],
  },
]
