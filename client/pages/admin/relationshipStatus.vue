<template>
    <div>
      <div id="sc-page-wrapper">
           <!-- Top navigation ***************** start *************-->
        <div id="sc-page-top-bar" class="sc-top-bar">
             <div class="sc-top-bar-content uk-flex uk-flex-1">
				<h1 class="sc-top-bar-title uk-flex-1">
					Relationship Status
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
        <!-- Top Navigation ****************** end ************ -->
		<div id="sc-page-content">
 <section class="w-full flex justify-center items-center my-10">
   <center >
        <div class="form-con">
      <form class="" @submit.prevent="sendData">
       <div class="form-con-items">
             <div class="form-group">
        <label><h4>Relationship Status</h4></label>
        <div class="input wrapper flex items-center" 
          v-for="(input, index) in relationship"
          :key="`phoneInput-${index}`"
        >
         <div class="form-con-input">
            <input 
               v-model="input.name"
               type="text" 
               placeholder="i.e. Married"
               class="form-control" 
               style="margin-right:10px; margin-top:10px;"  
          />

         <b-icon icon="dash-circle-fill" 
          v-show="relationship.length > 1"  
          @click="removeField(index, relationship)" 
          font-scale="1.5"
          variant="warning"
          >
          </b-icon>
         </div>

        </div>
      </div>
      <!-- incr -->
      <div class="input-plus">
         <div></div>
         <div>
           <b-button @click="addField(input, relationship)" variant="primary" >
              <b-icon icon="plus-circle-fill" font-scale="1.5" > </b-icon>  Add
           </b-button>
         </div>
       </div>
      <!-- incr -->
      <div class="form-spacer"></div>
      <div><b-button type="submit" block squared="squared" style="background:#d9d9d9; border:none; color:#1a1a1a">Submit</b-button></div>
       </div>
    </form>
      </div> 
    </center>    
  </section>
  </div>
	</div>
    </div>
</template>

<script>
export default {
    name:"relationshipStatus",
    layout:"defaultV1",
    data() {
    return {
      relationship: [{ name:"" }],
    };
  },
  methods: {
    addField(name, fieldType) {
      fieldType.push({name:""});
    },
    removeField(index, fieldType) {
      fieldType.splice(index, 1)
    },
    sendData(){
        console.warn(this.relationship)
    }
  },
	
}
</script>

<style scoped>
#Dash-con{
	margin-left: 300px;
}
.form-con{
  background: white;
  max-width: 700px;
  box-shadow: 0px 2px 2px grey;
  padding: 20px 0px 0px 0px;
}
.form-con-input{
  display: flex;
  padding: 0px 20px 0px 20px;
}
.input-plus{
  display: flex;
  justify-content: space-between;
  margin-right: 20px;
  margin-bottom: 5px;
}
.form-con-items{
    display: flex;
    flex-direction: column;
}
.form-spacer{
    flex: 1;
}
</style>
    
