
<template>
	<div id="sc-page-wrapper">
		<div id="sc-page-content">
			<h1>Forms</h1>

        <section class="w-full flex justify-center items-center my-10">
    <div class="form-con">
      <form class="" @submit.prevent="sendData">
      <div class="form-group">
        <label class="text-gray-600 font-semibold text-lg">Phone Number</label>
        <div class="input wrapper flex items-center" 
          v-for="(input, index) in phoneNumbers"
          :key="`phoneInput-${index}`"
        >
         <div class="form-con-input">
            <input 
               v-model="input.phone"
               type="text" 
               placeholder=" Enter Phone Number"
               class="form-control" 
               style="margin-right:10px; margin-top:10px;"  
          />

          <input 
               v-model="input.name"
               type="text" 
               placeholder=" Enter name"
               class="form-control" 
               style="margin-right:10px; margin-top:10px;"  
          />

         <b-icon icon="dash-circle-fill" 
          v-show="phoneNumbers.length > 1"  
          @click="removeField(index, phoneNumbers)" 
          font-scale="1.5"
          variant="warning"
          >
          </b-icon>
         </div>

        </div>
      </div>
      <br>
      <!-- <b-button type="submit" variant="success">Submit</b-button> -->
    </form>
       <div class="input-plus">
         <div></div>
         <div>
           <b-button @click="addField(input, phoneNumbers)" variant="primary" >
              <b-icon icon="plus-circle-fill" font-scale="1.5" > </b-icon>  Create
           </b-button>
         </div>
       </div>
      </div>      
  </section>
		</div>
	</div>
</template>
<script>
export default {
    name:"DcForm",
    layout:'defaultV1',
    data() {
    return {
      phoneNumbers: [{ phone: "", name:"" }],
    };
  },
  methods: {
    addField(phone, fieldType) {
      fieldType.push({ phone: "" , name:""});
    },
    removeField(index, fieldType) {
      fieldType.splice(index, 1)
    },
    sendData(){
        console.warn(this.phoneNumbers)
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
  width: 600px;
  border: 2px solid grey;
  padding: 20px 20px 20px 20px;
}
.form-con-input{
  display: flex;
}
.input-plus{
  display: flex;
  justify-content: space-between;
}
</style>
    
