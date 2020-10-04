import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _66dbefb8 = () => interopDefault(import('..\\pages\\Posts\\index.vue' /* webpackChunkName: "pages/Posts/index" */))
const _8cbf9e50 = () => interopDefault(import('..\\pages\\auth\\login.vue' /* webpackChunkName: "pages/auth/login" */))
const _c7535bf4 = () => interopDefault(import('..\\pages\\Posts\\create.vue' /* webpackChunkName: "pages/Posts/create" */))
const _11188060 = () => interopDefault(import('..\\pages\\Posts\\components\\Post.vue' /* webpackChunkName: "pages/Posts/components/Post" */))
const _89d51f3c = () => interopDefault(import('..\\pages\\Posts\\_id\\index.vue' /* webpackChunkName: "pages/Posts/_id/index" */))
const _68ee29ae = () => interopDefault(import('..\\pages\\index.vue' /* webpackChunkName: "pages/index" */))

// TODO: remove in Nuxt 3
const emptyFn = () => {}
const originalPush = Router.prototype.push
Router.prototype.push = function push (location, onComplete = emptyFn, onAbort) {
  return originalPush.call(this, location, onComplete, onAbort)
}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: decodeURI('/'),
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/Posts",
    component: _66dbefb8,
    name: "Posts"
  }, {
    path: "/auth/login",
    component: _8cbf9e50,
    name: "auth-login"
  }, {
    path: "/Posts/create",
    component: _c7535bf4,
    name: "Posts-create"
  }, {
    path: "/Posts/components/Post",
    component: _11188060,
    name: "Posts-components-Post"
  }, {
    path: "/Posts/:id",
    component: _89d51f3c,
    name: "Posts-id"
  }, {
    path: "/",
    component: _68ee29ae,
    name: "index"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
