const pkg = require('./package');
const path = require('path');
const serveFromSubFolder = false;

module.exports = {
	target: 'static',
	head: { htmlAttrs: {lang: 'en'},
		title: 'Scutum Admin',
		meta: [
			{ charset: 'utf-8' },
			{
				name: 'viewport',
				content: 'width=device-width, initial-scale=1'
			},
			{
				hid: 'description',
				name: 'description',
				content: pkg.description
			}
		],
		script: [
			{ src: (process.env.NODE_ENV !== 'production' || !serveFromSubFolder ? '' : '/' + dist ) + '/vendor/uikit.min.js'}
		],
		link: [
			{ rel: 'icon', type: 'image/x-icon', href: (process.env.NODE_ENV !== 'production' || !serveFromSubFolder ? '' :  '/' + dist ) + '/favicon.ico'},
			{ rel: 'preload', href: (process.env.NODE_ENV !== 'production' || !serveFromSubFolder ? '' : '/' + dist) + '/fonts/roboto_base64.css', as: 'style' },
			/// fonts
			{ rel: 'stylesheet', href: (process.env.NODE_ENV !== 'production' || !serveFromSubFolder ? '' : '/' + dist) + '/fonts/mdi/css/materialdesignicons.css' },
		]
	},

	loading: {color: 'rgba(0,0,0,.8)'},
	loadingIndicator: {
		color: '#00838f',
		background: 'white'},

	css: ['uikit/dist/css/uikit.css'],

	plugins: [],
	rules: {"no-unused-vars": "off" },
	modules: [
		'@nuxtjs/axios',
		 // https://go.nuxtjs.dev/bootstrap
		 'bootstrap-vue/nuxt',
		 // https://go.nuxtjs.dev/pwa
		 '@nuxtjs/pwa',
	],
	axios: {baseURL:"http://127.0.0.1:8000"},
	bootstrapVue: {icons: true},
	manifest: {lang: 'en'},
	/*
	** Build configuration
	*/
	build: {
		// analyze: true,
		progress: true,
		babel: {
			plugins: [
				"@babel/plugin-transform-spread"
			],
			ignore: [
				"node_modules",
				"assets/js/vendor"
			]
		},
		extend (config, ctx) {
			if (ctx.isDev && ctx.isClient) {
				config.module.rules.push(
					// Run ESLint on save
					{
						enforce: 'pre',
						test: /\.(js|vue)$/,
						loader: 'eslint-loader',
						exclude: /(node_modules)/
					}
				);
			}
			// aliases
			config.resolve.alias['scss'] = path.resolve(__dirname, './assets/scss');
			// adjust path when serving app from sub-folder
			if (!ctx.isDev && serveFromSubFolder) {
				config.output.publicPath = '/' + dist + '/_nuxt/';
			}
			return config;
		}
	},
	router: {
		middleware: ['redirect'],
		
	// 	extendRoutes(routes, resolve) {
	
	// 	  routes.push({
	// 		name: 'Categorys',
	// 		path: '/:category_slug/',
	// 		component: resolve(__dirname, 'pages/Category.vue')
	// 	  })
	//   }
	},
}