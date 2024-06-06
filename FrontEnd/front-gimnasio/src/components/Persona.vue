<template>
  <form>
    <div class="relative w-full mb-3">
      <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2" htmlfor="grid-password"> Name</label>
      <input type="text" class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150" placeholder="Name">
    </div>

    <div class="relative w-full mb-3">
      <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2" htmlfor="grid-password">Last Name</label>
      <input type="text" class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150" placeholder="Last Name">
    </div>

    <div class="relative w-full mb-3">
      <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2" htmlfor="grid-password">Title</label>
      <input type="text" class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150" placeholder="Title">
    </div>

    <div class="relative w-full mb-3">
      <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2" htmlfor="grid-password">Date of Birth</label>
      <input type="date" class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150">
    </div>

    <div class="relative w-full mb-3">
      <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2" htmlfor="grid-password">Blood Type</label>
      <input type="text" class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150" placeholder="Blood Type">
    </div>

    <div class="relative w-full mb-3">
      <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2" htmlfor="grid-password">Gender</label>
      <select class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150">
        <option value="male">Male</option>
        <option value="female">Female</option>
        <option value="other">Other</option>
      </select>
    </div>

    <div class="relative w-full mb-3">
      <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2" htmlfor="grid-password">Photo</label>
      <input type="file" class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150">
    </div>

    <div class="text-center mt-6">
      <button class="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150" type="button">
        Crear Cuenta
      </button>
    </div>
  </form>
</template>   