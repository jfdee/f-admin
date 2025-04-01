export default [
  {
    path: 'admin',
    name: 'admin-components-page',
    component: () => import ('./Page.vue'),
    children: [
      {
        path: ':code',
        name: 'admin-components-workspace-view',
        component: () => import('./workspace/View.vue'),
      },
    ],
  },
]
