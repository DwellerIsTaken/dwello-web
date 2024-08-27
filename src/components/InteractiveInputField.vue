<!--<template>
  <div class="w-72">
    <div :class="borderClass">
      <input
        class="peer h-full w-full rounded-[7px] border bg-transparent px-3 py-2.5 font-sans text-sm font-normal outline outline-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-pink-500 focus:border-t-transparent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50"
        placeholder=" "
      />
      <label :class="labelClass">
        Required
      </label>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    //borderColor: {
      //type: String,
      //default: "border-blue-gray-200",
    //},
    labelColor: {
      type: String,
      default: "#ffffff",
    },
    width: {
      type: String,
      default: "50rem",
    }
  },
  data() {
    return {
      borderClass: `relative h-10 w-full min-w-[${this.width}]`,
      labelClass: `before:content[\' \'] after:content[\' \'] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none text-[11px] font-normal leading-tight transition-all before:pointer-events-none before:mt-[6.5px] before:mr-1 before:box-border before:block before:h-1.5 before:w-2.5 before:rounded-tl-md before:border-t before:border-l before:transition-all after:pointer-events-none after:mt-[6.5px] after:ml-1 after:box-border after:block after:h-1.5 after:w-2.5 after:flex-grow after:rounded-tr-md after:border-t after:border-r after:transition-all peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[3.75] peer-placeholder-shown:before:border-transparent peer-placeholder-shown:after:border-transparent peer-focus:text-[11px] peer-focus:leading-tight peer-disabled:text-transparent peer-disabled:before:border-transparent peer-disabled:after:border-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500 bg-[${this.labelColor}]`,
    };
  },
};
</script>-->

<!--<script setup>
  import { defineProps } from 'vue';

  defineProps({
    width: String,
    borderColor: String,
    labelColor: String
  });

  const borderClass = `relative h-10 w-full min-w-[${this.width}]`;
  const labelClass = 'before:content[\' \'] after:content[\' \'] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none text-[11px] font-normal leading-tight transition-all before:pointer-events-none before:mt-[6.5px] before:mr-1 before:box-border before:block before:h-1.5 before:w-2.5 before:rounded-tl-md before:border-t before:border-l before:transition-all after:pointer-events-none after:mt-[6.5px] after:ml-1 after:box-border after:block after:h-1.5 after:w-2.5 after:flex-grow after:rounded-tr-md after:border-t after:border-r after:transition-all peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[3.75] peer-placeholder-shown:before:border-transparent peer-placeholder-shown:after:border-transparent peer-focus:text-[11px] peer-focus:leading-tight peer-disabled:text-transparent peer-disabled:before:border-transparent peer-disabled:after:border-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500 ' + props.labelColor;
</script>-->

<!--<template>
  <input
    :class="computedClasses"
    type="text"
    :placeholder="placeholder"
  />
</template>

<script>
export default {
  props: {
    color: {
      type: String,
      default: "bg-red-300",
    },
    placeholder: {
      type: String,
      default: "Enter text...",
    },
  },
  computed: {
    computedClasses() {
      // Combine default classes with custom classes passed via props
      return `border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 rounded-3xl ${this.color}`;
    },
  },
};
</script>-->

      
<!--<template>
  <div :class="box">
    <input
      :class="inputClass"
      placeholder=" "
    />
    <label :class="labelClass">
      Required
    </label>
  </div>
</template>

<script>
export default {
  props: {
    placeholderColor: {
      type: String,
      default: "#737373",
    },
    beforeColor: {
      type: String,
      default: "#B3B9C2",
    },
    afterColor: {
      type: String,
      default: "#007BFF",
    },
    height: {
      type: String,
      default: "2.5rem",
    },
    width: {
      type: String,
      default: "30rem",
    },
  },
  computed: {
    box() {
      return `m-4 relative min-h-[${this.height}] min-w-[${this.width}]`;
    },
    inputClass() {
      return `peer h-full w-full rounded-[7px] border-b border-x border-[${this.beforeColor}] bg-transparent px-3 py-2.5 font-sans text-sm font-normal text-[${this.beforeColor}] outline outline-0 transition-all placeholder-shown:border placeholder-shown:border-[${this.beforeColor}] placeholder-shown:border-t-[${this.beforeColor}] focus:border-2 focus:border-[${this.afterColor}] focus:border-t-transparent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50`;
    },
    labelClass() {
      return `before:content[' '] after:content[' '] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none text-[11px] font-normal leading-tight placeholder-text-[${this.placeholderColor}] text-[${this.placeholderColor}] transition-all before:pointer-events-none before:mt-[6.5px] before:mr-1 before:box-border before:block before:h-1.5 before:w-2.5 before:rounded-tl-md before:border-t before:border-l before:border-[${this.beforeColor}] before:transition-all after:pointer-events-none after:mt-[6.5px] after:ml-1 after:box-border after:block after:h-1.5 after:w-2.5 after:flex-grow after:rounded-tr-md after:border-t after:border-r after:border-[${this.beforeColor}] after:transition-all peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[3.75] peer-placeholder-shown:text-[${this.beforeColor}] peer-placeholder-shown:before:border-transparent peer-placeholder-shown:after:border-transparent peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-red-500 peer-focus:before:border-t-2 peer-focus:before:border-l-2 peer-focus:before:border-red-500 peer-focus:after:border-t-2 peer-focus:after:border-r-2 peer-focus:after:border-red-500 peer-disabled:text-transparent peer-disabled:before:border-transparent peer-disabled:after:border-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500`;
    }
  },
  mounted() {
    console.log(this.inputClass);
    console.log(this.labelClass);
  }
};
</script>
-->

<!-- Without tw-elements, only problem is the line keeps appearing when the text is inputted and you start to zoom in and out-->
<template>
  <div class="m-4 relative min-h-10 min-w-72">
    <input
      class="peer h-full w-full rounded-[7px] border-b border-x border-blue-gray-200 bg-transparent px-3 py-2.5 font-sans text-sm font-normal text-blue-gray-700 outline outline-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-pink-500 focus:border-t-transparent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50"
      placeholder=" "
    />
    <label class="before:content[' '] after:content[' '] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none text-[11px] font-normal leading-tight text-blue-gray-400 transition-all before:pointer-events-none before:mt-[6.5px] before:mr-1 before:box-border before:block before:h-1.5 before:w-2.5 before:rounded-tl-md before:border-t before:border-l before:border-blue-gray-200 before:transition-all after:pointer-events-none after:mt-[6.5px] after:ml-1 after:box-border after:block after:h-1.5 after:w-2.5 after:flex-grow after:rounded-tr-md after:border-t after:border-r after:border-blue-gray-200 after:transition-all peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[3.75] peer-placeholder-shown:text-blue-gray-500 peer-placeholder-shown:before:border-transparent peer-placeholder-shown:after:border-transparent peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-pink-500 peer-focus:before:border-t-2 peer-focus:before:border-l-2 peer-focus:before:border-pink-500 peer-focus:after:border-t-2 peer-focus:after:border-r-2 peer-focus:after:border-pink-500 peer-disabled:text-transparent peer-disabled:before:border-transparent peer-disabled:after:border-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500">
      Required
    </label>
  </div>
</template>




    

    

    