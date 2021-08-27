
<template>
	<div id="sc-page-wrapper">
		<div id="sc-page-content">
			<h1>Dashboard</h1>
		<DcButton buttonType="button" value="Add New Record" href="https://google.com" icon="arrow-up" />
		<br>
		<br>
		<b-button @click="successTest" variant="success">Success Alert</b-button>
		<b-button @click="errorTest" variant="danger">Error Alert</b-button>
		<b-button @click="infoTest" variant="info">Info Alert</b-button>
		<b-button @click="deleteTest('danger')" variant="danger">Delete Alert</b-button>

		 <div>
			 <DcMessages :message="message"/>
			  <DcMessages :info="info" />
			   <DcMessages :error="errors"/>
        </div>
		</div>
	</div>
</template>

<script>
import DcButton from '../../components/Components/button.vue'
import DcMessages from '../../components/Components/messages.vue'
export default {
  components: { DcMessages, DcButton },
  layout: 'accDefault',

  data(){
	  return{
		  message:'',
		  errors:null,
		  info:''
	  }
  },

  methods:{
	  successTest(){
		  this.message='Your work have been Saved'
		  
		   this.$bvToast.toast('Your work have been Saved', {
			title: 'Success',
			autoHideDelay: 2000,
			solid: true
        })
	  },
	  errorTest(){
		  this.errors='Something went wrong....try again later'
	  },
	  infoTest(){
		  this.info='It has survived not only five centuries. but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages';
	  },
	  deleteTest(variant = null){
		Swal.fire({
		title: 'Are you sure?',
		text: "You won't be able to revert this!",
		icon: 'warning',
		showCancelButton: true,
		confirmButtonColor: '#3085d6',
		cancelButtonColor: '#d33',
		confirmButtonText: 'Yes, delete it!'
		}).then((result) => {
		if (result.isConfirmed) {
			Swal.fire({
				title:'Deleted!',
				text: 'Your file has been deleted.',
				icon:'success',
				showConfirmButton: false,
				timer: 1500
				})
			this.$bvToast.toast('Your file has been deleted. auto-hide is enabled, while you hover over the toast, the auto-hide countdown will pause', {
            title: 'Deleted!',
			autoHideDelay: 1500,
            variant: variant,
            solid: true
        })
		}
		})
	  },

	   makeToast(variant = null) {
        this.$bvToast.toast('Toast body content', {
          title: `Variant ${variant || 'default'}`,
          variant: variant,
          solid: true
        })
      }
  }
	
}
</script>

<style scoped>
#Dash-con{
	margin-left: 300px;
}
</style>