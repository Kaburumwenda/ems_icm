<template>
	<aside id="sc-sidebar-main" class="sc-sidebar-info-fixed">
		<div id="sc-sidebar-main-offcanvas-bar" v-touch:swipe.left="closeSidebar" class="uk-offcanvas-bar">
			
			<div class="sc-sidebar-main-scrollable" data-sc-scrollbar="visible-y">
				<div id="s" class="menu-title">
				  <span class="material-icons menu-s-icon">dashboard</span>
				  <span class="menu-txt">Client Side</span>
			    </div>
				<ScMenuList :menu-data="menuEntrie" :accountData="menuAccount" :is-parent="true"></ScMenuList>
				<div class="sidemenu-con">
					
				</div>
			</div>
			<div class="sc-sidebar-info">
			</div>
		</div>
	</aside>
</template>

<script>
import { mapState } from 'vuex'
import ScMenuList from './navigation/MenuList';
import { scMq } from '~/assets/js/utils'
import { menuEntries } from './navigation/sidebar_menu'
import {menuAccount} from '../data/menu'
import {AES, enc}from 'crypto-js';


require('~/plugins/vue2-touch-events')

export default {
	name: 'ScSidebar',
	components: {
		ScMenuList
	},
	data(){
		return{
			menuAccount,
			menuCat:[],
			menuEntries,
			menuEntrie:[],
		    category:{},
			secrectKey:'MYKEY4DEMO3R@RTDGH56%RTYF4FYU'
		}
	},
	// data: () => ({
	// 	menuEntries,
	// 	category:{},
	// }),
	computed: mapState([
		'vxSidebarMainExpanded',
		'vxAppVersion'
	]),
	watch: {
		'vxSidebarMainExpanded' (state) {
			if(scMq.mediumMax() || this.$store.getters['sidebarOffcanvasState']) {
				if (state) {
					UIkit.offcanvas('#sc-sidebar-main').show();
					if(this.$store.getters.offcanvasState) {
						this.$store.commit('offcanvasToggle', false);
					}
				} else {
					UIkit.offcanvas('#sc-sidebar-main').hide();
				}
			}
		},
		$route () {
			this.$nextTick(() => {
				if(scMq.mediumMax()) {
					this.$store.commit('sidebarMainToggle', false);
				}
			})
		}
	},
	mounted () {
		this.getCategory();
		this.getmenuData();
		const self = this;
		this.$nextTick(() => {
			if(scMq.mediumMax() || this.$store.getters['sidebarOffcanvasState']) {
				// activate UIKit offcanvas
				UIkit.offcanvas(document.getElementById('sc-sidebar-main'), {
					overlay: true,
					container: '#nuxt-wrapper'
				});
				// update drop container
				UIkit.util.on('#sc-sidebar-main', 'hidden', function () {
					self.$store.commit('sidebarMainToggle', false);
				});
				self.$store.commit('sidebarMainToggle', false);
			}
		})
	},
	methods: {
		 async getCategory(){
         await this.$axios.$get("/api/v1/category2")
          .then(resp =>{
			  this.menuEntrie = resp;
            // const menuApiData = AES.encrypt(JSON.stringify(resp),this.secrectKey);
            // localStorage.setItem('menuApiData', menuApiData.toString());
			})
        },
		getmenuData(){
			// const decrypted2 = AES.decrypt(localStorage.getItem('menuApiData'), this.secrectKey);
		    // const decryptedObject = decrypted2.toString(enc.Utf8);
		    // var dataq = JSON.parse(decryptedObject)
			// this.menuEntrie = dataq;				
			},

		closeSidebar (direction, event) {
			if (event.type === 'touchend') {
				this.$store.commit('sidebarMainToggle', false);
			}
		},
	}
}
</script>

<style scoped>
.icon-con{
	display: flex;
	justify-content:flex-start;
}
.sid-txt{
	margin-left: 20px;
}
.sidemenu-con{
	margin-top: 10px;
}
.sidemenu-con ul li{
	list-style: none;
}
.sidemenu-btn{
	background: transparent;
	color: black;
	border: none;
}
.sidemenu-btn:hover{
	background: olive;
}
/************ sidebar menu top */
.menu-title{
	height:52px;
	box-shadow: 0 2px 2px -2px gray;
	display: flex;
	align-items: center;
}
.menu-txt{
	font-size: 14px;
	font-weight: bold;
	color: grey;
	margin-left: 20px;
}
.menu-s-icon{
	margin-left: 20px;
	color: grey;
}
</style>
