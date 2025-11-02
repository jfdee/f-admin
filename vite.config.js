import { defineConfig, loadEnv } from 'vite'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'

import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'
import vue from '@vitejs/plugin-vue'
import {fileURLToPath} from 'node:url'

export default ({ mode }) => {
  const env = loadEnv(mode, process.cwd())

  const PORT = env.VITE_PORT
  const SERVER_HOST = env.VITE_SERVER_HOST
  console.log(SERVER_HOST)
  return defineConfig({
    root: 'src',
    server: {
      port: PORT,
      proxy: {
        '/api': {
          target: SERVER_HOST,
          changeOrigin: true,
        },
      },
    },
    plugins: [
      vue(),
      AutoImport({
        resolvers: [ElementPlusResolver()],
      }),
      Components({
        resolvers: [ElementPlusResolver()],
      }),
    ],
    resolve: {
      alias: [
        {find: '@', replacement: fileURLToPath(new URL('./src', import.meta.url))}
      ],
    },
  })
}
