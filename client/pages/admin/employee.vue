
<template>
	<div id="sc-page-wrapper">
        <div id="sc-page-top-bar" class="sc-top-bar">
             <div class="sc-top-bar-content uk-flex uk-flex-1">
				<h1 class="sc-top-bar-title uk-flex-1">
					Employee Registration
				</h1>
             
				<span class="uk-text-muted">
					Public
				</span>
				<div class="sc-actions uk-margin-left">
					<a href="javascript:void(0)" class="sc-actions-icon mdi mdi-filter-variant sc-js-el-hide md-color-red-800 uk-animation-shake" data-uk-toggle="target: #sc-page-top-bar; cls: sc-top-bar-expanded"></a>
					<a href="javascript:void(0)" class="sc-actions-icon mdi mdi-close sc-js-el-show" data-uk-toggle="target: #sc-page-top-bar; cls: sc-top-bar-expanded"></a>
				</div>
			</div>
        </div>

<!--- ****************************************************** CONTENT ************************ -->
		<div id="sc-page-content">
         <Profile/>
        </div>
<!--************************************************************** CONTENT **************** -->
<!-- DEMO ************* --> 
<!-- DEMO ******--> 
	</div>
</template>

<script>
import {VueTelInput} from 'vue-tel-input';
import 'vue-tel-input/dist/vue-tel-input.css';
import Profile from '../../components/employee/profile.vue';
import {countries} from '../../data/countries'


export default {
  components: { VueTelInput, Profile, },

    name:"Employee",
    layout:"defaultV1",
	 data(){
        return{
            cmp:"Profile",
            countries,
            value:'',
            country:'',
            gender:['Male', 'Female', 'Not sure', 'Rather not to say'],
            relationship:['Single', 'Married', 'Divorced', 'Complicated', 'Searching'],
            personal_identification_type:['National Identity', 'Passport', 'Military', 'Alien'],
            dependants: [{ name: "", birth:"", sex:"", relation:"" }],
            kin:[{ name: "", sex:"", relation:"", phone:"", email:"", postal:"", address:"" }]
        }
    },
    mounted(){
        this.KinDatatable();
    },
    methods: {
        updateCmp(item){
            this.cmp = item
        },
    addField(name, fieldType) {
      fieldType.push({ name: "", birth:"", sex:"", relation:"" });
    },
    removeField(index, fieldType) {
      fieldType.splice(index, 1)
    },
    // sendData(){
    //     console.warn(this.phoneNumbers)
    // },
    addKinField(name, fieldType) {
      fieldType.push({ name: "", sex:"", relation:"", phone:"", email:"", postal:"", address:"" });
	  this.KinDatatable();
    },
    KinDatatable(){
		let table = $("table#exampleaa").DataTable( {
           paging: false,
		   searching: false,
		   retrieve: true,
		   ordering: false,
		   info: false
        } );
    }
  },
}
</script>


<style scoped>
.form-con{
    background: white;
    padding: 20px 20px 20px 20px;
    border-radius: 10px;
}
label{
    font-weight:500;
    font-size: 18px;
}
sup{
    color: orangered;
    font-weight: bold;
    font-size:medium;
}
.emp-submit-btn{
    display: flex;
    align-items: center;
    justify-content: center;
}
/************************************ DEPENDANT BTN */
.dependants-incr-btn{
    display: flex;
    justify-content: space-between;
}
.dependants-incr-btn-items{
    display: flex;
    align-items: center;
}
.kin-form-tr{
		width: 300px !important;
	}
@media only screen and (max-width: 768px){
}
/**************************************************** DROPMENU ITEMS */
.drop-submenu-items{
    display: flex;
    align-items: center;
}

</style>