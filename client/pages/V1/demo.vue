<template>
    <div>
        <table >
        
     </table>
     <br>
     <br>
     <!-- <p>id="example" class="display dt-responsive" style="width:100%"</p> -->
     <!-- <p>v-for="item in rowData" :key="item"</p> -->
     <div>
    <table id="yourTable" class="display dt-responsive table-bordered" style="width:100%">
        <thead>
            <tr>
            <th >Mail</th>
            <th>Date</th>
            <th >Adress</th>
            <th >Company</th>
            <th >Number</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </tbody>
       
    </table>
    <br>
    <button @click="datademo">Add record</button>
</div>

    </div>
</template>

<script>
import button from '../../components/Components/button.vue';
export default {
  components: { button },
    name:"demo",
    mounted(){
       this.datademo()
    },
    methods:{
        datademo(){
            const table = $("#yourTable").DataTable();
            // const tr = $("<tr><td><input placeholder='dependants name' style='width:200px'></input></td><td>2</td><td>3</td><td>4</td> <td>5</td></tr>");
            // table.row.add(tr[0]).draw();
            
        }
    }
}
</script>