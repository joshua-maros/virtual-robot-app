<template>
    <div id='upload_form'> 
           <form id='config_file_form' action='/upload' method="POST" enctype=multipart/form-data> 
                <input type="file" id="myFile" name="file">
                <input type="submit">
            </form>
    </div>
</template>

<script >

export default {
  name: 'uploadButton',
}


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#config_file_form {
  position: absolute;
  top: 50%;
  right: 8%;
}

</style>
