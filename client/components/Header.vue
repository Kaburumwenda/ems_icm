<template>
	<header id="sc-header" ref="header">
		<nav class="uk-navbar uk-navbar-container" data-uk-navbar="mode: click; duration: 360">
			<div class="uk-navbar-left nav-overlay-small uk-margin-right uk-navbar-aside">
				<a v-if="!vxTopMenuActive && !vxSidebarMiniActive" id="sc-sidebar-main-toggle" href="javascript:void(0)" @click.stop="toggleMainSidebar">
					<i v-if="sidebarMainExpanded" class="mdi mdi-backburger" />
					<i v-else class="mdi mdi-menu" />
				</a>
				<div class="sc-brand uk-visible@m">
					<nuxt-link to="/">
						<img v-rjs="require('~/assets/img/logo@2x.png')" :src="logo" alt="">
					</nuxt-link>
				</div>
			</div>
			<div class="uk-navbar-left nav-overlay uk-margin-right">
				<nuxt-link to="/"><span style="color:white">EMS</span></nuxt-link>
			</div>

			<div class="nav-overlay nav-overlay-small uk-navbar-right">
				<ul class="uk-navbar-nav">

					<li>
						<a href="javascript:void(0)">
							<span class="mdi mdi-email"></span>
						</a>
						<div class="uk-navbar-dropdown sc-padding-remove">
							<div class="uk-panel uk-panel-scrollable uk-height-medium">
								<ul class="uk-list uk-list-divider">
									<li v-for="message in user.messages" :key="message.id" class="sc-list-group">
										<div class="sc-list-addon">
											<img v-if="message.avatar.image" :src="message.avatar.image" class="sc-avatar" alt="">
											<span v-if="!message.avatar.image" :title="message.from" :class="message.avatar.color" class="sc-avatar-initials">
												{{ message.from | initials }}
											</span>
										</div>
										<a href="javascript:void(0)" class="sc-list-body">
											<span class="uk-text-small uk-text-muted uk-width-expand">
												{{ message.date }}
											</span>
											<span class="uk-display-block uk-text-truncate">
												{{ message.content }}
											</span>
										</a>
									</li>
								</ul>
							</div>
							<nuxt-link to="/pages/mailbox" class="uk-flex uk-text-small sc-padding-small-ends sc-padding">
								Show all in mailbox
							</nuxt-link>
						</div>
					</li>
					<li class="uk-visible@l">
						<a href="javascript:void(0)">
							<span class="mdi mdi-bell uk-display-inline-block">
								<span v-show="!alertsEmpty" class="sc-indicator md-bg-color-red-600"></span>
							</span>
						</a>
						<div class="uk-navbar-dropdown md-bg-grey-100">
							<div class="sc-padding sc-padding-small-ends">
								<ul id="sc-header-alerts" class="uk-list uk-margin-remove">
									<li v-for="(alert, index) in user.alerts" :key="alert.id" :style="{'--index': index}" class="uk-margin-small-top sc-border sc-round md-bg-white">
										<div class="uk-flex uk-flex-middle">
											<div class="uk-margin-right uk-margin-small-left">
												<i class="mdi" :class="[alert.icon, alert.color]"></i>
											</div>
											<div class="uk-flex-1 uk-text-small">
												{{ alert.text }}
											</div>
										</div>
									</li>
								</ul>
							</div>
						</div>
					</li>
					<li>
						<a href="javascript:void(0)">
							<img v-rjs="require('~/assets/img/avatars/avatar_default_sm@2x.png')" :src="user.avatar" alt="">
						</a>
						<div class="uk-navbar-dropdown uk-dropdown-small">
							<ul class="uk-nav uk-nav-navbar">
								<li>
									<nuxt-link to="/pages/user_profile">
										Profile
									</nuxt-link>
								</li>
								<li>
									<nuxt-link to="/pages/settings">
										Settings
									</nuxt-link>
								</li>
								<li>
									<nuxt-link to="/accounts/login">
										Login
									</nuxt-link>
								</li>
							</ul>
						</div>
					</li>

					<li>
						<a href="javascript:void(0)">
							<i class="mdi mdi-dots-vertical"></i>
						</a>
						<div class="uk-navbar-dropdown uk-dropdown-small">
							<ul class="uk-nav uk-nav-navbar">
								<li>
									<nuxt-link to="/" class="a-hover">
										Default
										<span class="material-icons">navigate_next</span>
									</nuxt-link>
								</li>
								<li>
									<nuxt-link to="/V2/accounts/" class="a-hover">
										Accounts
										<span class="material-icons">navigate_next</span>
									</nuxt-link>
								</li>
								<li>
									<nuxt-link to="/V3/events/" class="a-hover">
										Events
										<span class="material-icons">navigate_next</span>
									</nuxt-link>
								</li>
								<li>
									<nuxt-link to="/V3/events/" class="a-hover">
										Admin
										<span class="material-icons">navigate_next</span>
									</nuxt-link>
								</li>
								<li>
									<nuxt-link to="/V3/events/" class="a-hover">
										Importer
										<span class="material-icons">navigate_next</span>
									</nuxt-link>
								</li>
								<li>
									<nuxt-link to="/V3/events/" class="a-hover">
										Exporter
										<span class="material-icons">navigate_next</span>
									</nuxt-link>
								</li>
								<li>
									<nuxt-link to="/V3/events/" class="a-hover">
										Transporter
										<span class="material-icons">navigate_next</span>
									</nuxt-link>
								</li>
							</ul>
						</div>
					</li>

				</ul>
				<a v-if="vxOffcanvasPresent" href="javascript:void(0)" class="md-color-white uk-margin-left uk-hidden@l" @click="toggleOffcanvas">
					<i v-show="!vxOffcanvasExpanded" class="mdi mdi-menu"></i><i v-show="vxOffcanvasExpanded" class="mdi mdi-arrow-right"></i>
				</a>
			</div>
		</nav>
	</header>
</template>

<script>
import { mapState } from 'vuex'
import { scMq } from '~/assets/js/utils'
import ScTopMenu from '~/components/topmenu/TopMenu.vue';
import { scHelpers } from "~/assets/js/utils";
const { uniqueID } = scHelpers;

export default {
	name: 'ScHeader',
	components: {
		ScTopMenu
	},
	data: () => ({
		user: {
			avatar: require('~/assets/img/avatars/avatar_default_sm.png'),
			messages: [
				{
					"id": 1,
					"from": "Aaron Jensen",
					"avatar": {
						"image": require("~/assets/img/avatars/avatar_03_sm.png")
					},
					"date": "24-10-2019",
					"content": "Zelnavo dej foten tu bivgal wi lonuh cow wuvelo atilid taza wucacto uwa."
				},
			
			],
			alerts: [
				{
					id: 1,
					text: 'Information Page Not Found!',
					icon: 'mdi-alert-outline',
					color: 'md-color-red-600'
				},
				
			]
		},
	props:{
		menuSelector:{
			type:Boolean,
			default:false
		}
	},
		sidebarMainExpanded: true,
		offcanvasExpanded: false,
		offcanvasPresent: false,
		logo: require('~/assets/img/logo.png'),
		alertsEmpty: null,
		topMenuData: [
			{
				id: uniqueID(),
				title: "Mailbox",
				url: '/pages/mailbox'
			},
			{
				id: uniqueID(),
				title: "Components",
				url: null,
				isOpen: false,
				submenu: [
					{
						id: uniqueID(),
						title: "Accordion",
						url: '/components/accordion'
					},
					{
						id: uniqueID(),
						title: "Alert",
						url: '/components/alert'
					},
					{
						id: uniqueID(),
						title: "Avatars",
						url: '/components/avatars'
					},
					{
						id: uniqueID(),
						title: "Grid",
						url: '/components/grid'
					}
				]
			},
			{
				id: uniqueID(),
				title: "Pages",
				url: null,
				isOpen: false,
				submenu: [
					{
						id: uniqueID(),
						title: "Blank",
						url: '/pages/blank'
					},
					{
						id: uniqueID(),
						title: "Gallery",
						url: '/pages/gallery'
					},
					{
						id: uniqueID(),
						title: "Settings",
						url: '/pages/settings'
					}
				]
			},
			{
				id: uniqueID(),
				title: "Nested",
				url: null,
				isOpen: false,
				submenu: [
					{
						id: uniqueID(),
						title: "Level 1",
						url: null,
					},
					{
						id: uniqueID(),
						title: "Level 1",
						url: null,
						isOpen: false,
						submenu: [
							{
								id: uniqueID(),
								title: "Sub-level 1.1",
								url: null
							},
							{
								id: uniqueID(),
								title: "Sub-level 1.1",
								url: null
							},
							{
								id: uniqueID(),
								title: "Sub-level 1.1",
								url: null,
								isOpen: false,
								submenu: [
									{
										id: uniqueID(),
										title: "Sub-level 1.1.1",
										url: null
									},
									{
										id: uniqueID(),
										title: "Sub-level 1.1.1",
										url: null
									},
									{
										id: uniqueID(),
										title: "Sub-level 1.1.1",
										url: null
									},
									{
										id: uniqueID(),
										title: "Sub-level 1.1.1",
										url: null
									},
									{
										id: uniqueID(),
										title: "Sub-level 1.1.1",
										url: null
									}
								]
							},
							{
								id: uniqueID(),
								title: "Sub-level 1.1",
								url: null
							},
							{
								id: uniqueID(),
								title: "Sub-level 1.1",
								url: null
							}
						]
					},
					{
						id: uniqueID(),
						title: "Level 1",
						url: null,
					},
					{
						id: uniqueID(),
						title: "Level 1",
						url: null,
					}
				]
			}
		],
	
	}),
	computed: {
		...mapState([
			'vxSidebarMainExpanded',
			'vxOffcanvasPresent',
			'vxOffcanvasExpanded',
			'vxTopMenuActive',
			'vxActiveLocale',
			'vxSidebarMiniActive'
		])
	},
	watch: {
		'vxSidebarMainExpanded' (state) {
			this.sidebarMainExpanded = state;
		},
		'vxOffcanvasExpanded' (state) {
			this.offcanvasExpanded = state;
		},
		'vxOffcanvasPresent' (state) {
			this.offcanvasPresent = state;
		}
	},
	mounted () {
		const self = this;
		self.$nextTick(() => {
			if(scMq.mediumMin() || this.$store.getters['sidebarOffcanvasState']) {
				self.sidebarMainExpanded = this.vxSidebarMainExpanded;
			} else {
				self.sidebarMainExpanded = false;
			}
		});
		// sticky header
		var options = scMq.mediumMax() ? { showOnUp: true, animation: "uk-animation-slide-top" } : {};
		UIkit.sticky(this.$refs.header, options);
	},
	methods: {
		menuSelector(){
			this.menuSelector = !this.menuSelector;
			console.warn(this.menuSelector);
		},
		toggleMainSidebar () {
			let state = !this.sidebarMainExpanded;
			this.$store.commit('sidebarMainToggle', state);
		},
		toggleOffcanvas () {
			let state = !this.offcanvasExpanded;
			this.$store.commit('offcanvasToggle', state);
		},
		updateLocale (event, code) {
			if (code === this.vxActiveLocale) {
				event.preventDefault();
			}
			this.$i18n.setLocale(code);
			this.$store.commit('updateLocale', code);
			this.isActiveLang(code)
		},
		isActiveLang (code) {
			return code === this.vxActiveLocale
		}
	}
}
</script>

<style scoped>
.a-hover:hover{
	background: gray;
}
</style>
