Code is working and checked in.  

Published to Azure and available at:

    rand64ints - [httpTrigger]
        Invoke url: https://randomnumberfunction.azurewebsites.net/api/rand64ints
        or https://randomnumberfunction.azurewebsites.net/api/rand64ints?count=10000&output=json
        or https://randomnumberfunction.azurewebsites.net/api/rand64ints?count=10000&output=string  <-- this one is the most fun
          

    rand32ints - [httpTrigger]
        Invoke url: https://randomnumberfunction.azurewebsites.net/api/rand32ints
        or https://randomnumberfunction.azurewebsites.net/api/rand16ints?count=10000&output=string 
        or https://randomnumberfunction.azurewebsites.net/api/rand16ints?count=10000&output=json 

These support the same parameters as above: 
    rand16ints - [httpTrigger]
        Invoke url: https://randomnumberfunction.azurewebsites.net/api/rand64ints

    randbytes - [httpTrigger]
        Invoke url: https://randomnumberfunction.azurewebsites.net/api/randbytes

    randuints - [httpTrigger]
        Invoke url: https://randomnumberfunction.azurewebsites.net/api/randuints

Ultimately will be used in a demo project, possibly React or React native.
