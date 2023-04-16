import adminRoutes from '/components/routes'
export default [
  {
    path: '/',
    redirect: r => ({name: 'components-admin-view', params: r.params}),
    children: [...adminRoutes],
  },
]
