# enctype
form 加上enctype="multipart/form-data"和不加上两种情况下，flask request接收到的数据不一样

如果要上传file，而且要通过flask request files来获取file，form应该加上 enctype