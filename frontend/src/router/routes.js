import adminRoutes from '@/components/routes'
export default [
  {
    path: '/',
    redirect: r => ({name: 'admin-components-page', params: r.params}),
    children: [...adminRoutes],
  },
]
