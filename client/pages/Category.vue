<template>
 <div id="cat-con">

      <h1>Category</h1>
      <br>
     <div>
        <h1>{{ category.name }}</h1>
        <h2>ID No.{{ category.id }}</h2>
     </div>
     <hr>
     <div v-for="rs in category.products" :key="rs.id">
         <img :src="rs.get_image" style="width:150px"/>
         <h4>Ksh: {{ rs.Sprice }}</h4>
         <p>{{ rs.title }}</p>
     </div>
     
 </div>
</template>

<script>
export default {
    name:"Category",
    data(){
        return{
            category: {
                products: []
            },
        }
    },
    mounted(){
        this.getCategory();
    },
     watch: {
        $route(to, from) {
            if (to.name === 'Category') {
                this.getCategory()
            }
        }
    },
    methods:{
        async getCategory() {
        const categorySlug = this.$route.params.category_slug
        await this.$axios.$get(`/api/v1/products/${categorySlug}/`)
            .then(response => {
                this.category = response;
                document.title = this.category.name + ' | demo'
            })
            .catch(error => {
                console.log(error)
            })
    },
    }
}
</script>


<style scoped>
#cat-con{
	margin-left: 300px;
}
</style>