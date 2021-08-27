<template>
    <div>
        <table id="myTable" class="table table-bordered table-striped table-hover dt-responsive nowrap" style="width:100%">
        <thead>
            <tr>
                <th>ID</th>
                <th>district</th>
                <th>beat</th>
                <th>address</th>
                <th>grid</th>
                <th>crimedescr</th>
                <th>ucr_ncic_code</th>
                <th>cdatetime</th>
                <th>latitude</th>
                <th>longitude</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="rs in tabledata" :key="rs">
                <td>{{rs.id}}</td>
                <td>{{ rs.district}}</td>
                <td>{{ rs.beat}}</td>
                <td>{{ rs.address}}</td>
                <td>{{ rs.grid}}</td>
                <td>{{ rs.crimedescr}}</td>
                <td>{{ rs.ucr_ncic_code}}</td>
                <td>{{ rs.cdatetime}}</td>
                <td>{{ rs.latitude}}</td>
                <td>{{ rs.longitude}}</td>
            </tr>
            
        </tbody>
    </table>

    <script>
       $(document).ready( function () {
          $('#myTable').DataTable();
      } );
    </script>
    </div>
</template>

<script>
export default {
    name:"MyTable",
    props:{
        tabledata:{
            type:Array,
            default:null
        }
    },

    mounted(){
        this.dynamicTable();
    },
    methods:{
        dynamicTable(){
           console.warn(this.tabledata);
        }
    },
}
</script>

<style scoped>
table{
    background: white;
}
</style>