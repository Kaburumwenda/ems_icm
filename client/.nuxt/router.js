import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _b5e6386c = () => interopDefault(import('../pages/Category.vue' /* webpackChunkName: "pages/Category" */))
const _16603670 = () => interopDefault(import('../pages/form.vue' /* webpackChunkName: "pages/form" */))
const _543bfe5c = () => interopDefault(import('../pages/table.vue' /* webpackChunkName: "pages/table" */))
const _c4ad62a8 = () => interopDefault(import('../pages/accounts/login.vue' /* webpackChunkName: "pages/accounts/login" */))
const _c19ca44c = () => interopDefault(import('../pages/admin/country.vue' /* webpackChunkName: "pages/admin/country" */))
const _11aa96d8 = () => interopDefault(import('../pages/admin/dashboard.vue' /* webpackChunkName: "pages/admin/dashboard" */))
const _21f30ebe = () => interopDefault(import('../pages/admin/department.vue' /* webpackChunkName: "pages/admin/department" */))
const _eb5dedcc = () => interopDefault(import('../pages/admin/employee.vue' /* webpackChunkName: "pages/admin/employee" */))
const _29b90e9c = () => interopDefault(import('../pages/admin/employmentType.vue' /* webpackChunkName: "pages/admin/employmentType" */))
const _3f1d0ea6 = () => interopDefault(import('../pages/admin/gender.vue' /* webpackChunkName: "pages/admin/gender" */))
const _15dfd44c = () => interopDefault(import('../pages/admin/identification.vue' /* webpackChunkName: "pages/admin/identification" */))
const _14914b38 = () => interopDefault(import('../pages/admin/referee.vue' /* webpackChunkName: "pages/admin/referee" */))
const _31efb894 = () => interopDefault(import('../pages/admin/relationshipStatus.vue' /* webpackChunkName: "pages/admin/relationshipStatus" */))
const _197795a9 = () => interopDefault(import('../pages/admin/section.vue' /* webpackChunkName: "pages/admin/section" */))
const _f1c57a32 = () => interopDefault(import('../pages/admin/statutory.vue' /* webpackChunkName: "pages/admin/statutory" */))
const _c6185bf2 = () => interopDefault(import('../pages/admin/workHistory.vue' /* webpackChunkName: "pages/admin/workHistory" */))
const _597f9177 = () => interopDefault(import('../pages/forms/wizard.vue' /* webpackChunkName: "pages/forms/wizard" */))
const _e3516966 = () => interopDefault(import('../pages/forms/wizard/step1.vue' /* webpackChunkName: "pages/forms/wizard/step1" */))
const _e3353a64 = () => interopDefault(import('../pages/forms/wizard/step2.vue' /* webpackChunkName: "pages/forms/wizard/step2" */))
const _e3190b62 = () => interopDefault(import('../pages/forms/wizard/step3.vue' /* webpackChunkName: "pages/forms/wizard/step3" */))
const _728a8f7c = () => interopDefault(import('../pages/V1/dataTable.vue' /* webpackChunkName: "pages/V1/dataTable" */))
const _47261a5b = () => interopDefault(import('../pages/V1/demo.vue' /* webpackChunkName: "pages/V1/demo" */))
const _15d58f06 = () => interopDefault(import('../pages/V2/accounts.vue' /* webpackChunkName: "pages/V2/accounts" */))
const _150b3562 = () => interopDefault(import('../pages/V3/events.vue' /* webpackChunkName: "pages/V3/events" */))
const _613d4d92 = () => interopDefault(import('../pages/admin/forms/wizard.vue' /* webpackChunkName: "pages/admin/forms/wizard" */))
const _079779e6 = () => interopDefault(import('../pages/admin/forms/wizard/step1.vue' /* webpackChunkName: "pages/admin/forms/wizard/step1" */))
const _077b4ae4 = () => interopDefault(import('../pages/admin/forms/wizard/step2.vue' /* webpackChunkName: "pages/admin/forms/wizard/step2" */))
const _075f1be2 = () => interopDefault(import('../pages/admin/forms/wizard/step3.vue' /* webpackChunkName: "pages/admin/forms/wizard/step3" */))
const _0742ece0 = () => interopDefault(import('../pages/admin/forms/wizard/step4.vue' /* webpackChunkName: "pages/admin/forms/wizard/step4" */))
const _0726bdde = () => interopDefault(import('../pages/admin/forms/wizard/step5.vue' /* webpackChunkName: "pages/admin/forms/wizard/step5" */))
const _61080fa6 = () => interopDefault(import('../pages/admin/wizard/step1.vue' /* webpackChunkName: "pages/admin/wizard/step1" */))
const _1c46cbd6 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/Category",
    component: _b5e6386c,
    name: "Category"
  }, {
    path: "/form",
    component: _16603670,
    name: "form"
  }, {
    path: "/table",
    component: _543bfe5c,
    name: "table"
  }, {
    path: "/accounts/login",
    component: _c4ad62a8,
    name: "accounts-login"
  }, {
    path: "/admin/country",
    component: _c19ca44c,
    name: "admin-country"
  }, {
    path: "/admin/dashboard",
    component: _11aa96d8,
    name: "admin-dashboard"
  }, {
    path: "/admin/department",
    component: _21f30ebe,
    name: "admin-department"
  }, {
    path: "/admin/employee",
    component: _eb5dedcc,
    name: "admin-employee"
  }, {
    path: "/admin/employmentType",
    component: _29b90e9c,
    name: "admin-employmentType"
  }, {
    path: "/admin/gender",
    component: _3f1d0ea6,
    name: "admin-gender"
  }, {
    path: "/admin/identification",
    component: _15dfd44c,
    name: "admin-identification"
  }, {
    path: "/admin/referee",
    component: _14914b38,
    name: "admin-referee"
  }, {
    path: "/admin/relationshipStatus",
    component: _31efb894,
    name: "admin-relationshipStatus"
  }, {
    path: "/admin/section",
    component: _197795a9,
    name: "admin-section"
  }, {
    path: "/admin/statutory",
    component: _f1c57a32,
    name: "admin-statutory"
  }, {
    path: "/admin/workHistory",
    component: _c6185bf2,
    name: "admin-workHistory"
  }, {
    path: "/forms/wizard",
    component: _597f9177,
    name: "forms-wizard",
    children: [{
      path: "step1",
      component: _e3516966,
      name: "forms-wizard-step1"
    }, {
      path: "step2",
      component: _e3353a64,
      name: "forms-wizard-step2"
    }, {
      path: "step3",
      component: _e3190b62,
      name: "forms-wizard-step3"
    }]
  }, {
    path: "/V1/dataTable",
    component: _728a8f7c,
    name: "V1-dataTable"
  }, {
    path: "/V1/demo",
    component: _47261a5b,
    name: "V1-demo"
  }, {
    path: "/V2/accounts",
    component: _15d58f06,
    name: "V2-accounts"
  }, {
    path: "/V3/events",
    component: _150b3562,
    name: "V3-events"
  }, {
    path: "/admin/forms/wizard",
    component: _613d4d92,
    name: "admin-forms-wizard",
    children: [{
      path: "step1",
      component: _079779e6,
      name: "admin-forms-wizard-step1"
    }, {
      path: "step2",
      component: _077b4ae4,
      name: "admin-forms-wizard-step2"
    }, {
      path: "step3",
      component: _075f1be2,
      name: "admin-forms-wizard-step3"
    }, {
      path: "step4",
      component: _0742ece0,
      name: "admin-forms-wizard-step4"
    }, {
      path: "step5",
      component: _0726bdde,
      name: "admin-forms-wizard-step5"
    }]
  }, {
    path: "/admin/wizard/step1",
    component: _61080fa6,
    name: "admin-wizard-step1"
  }, {
    path: "/",
    component: _1c46cbd6,
    name: "index"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config._app && config._app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
