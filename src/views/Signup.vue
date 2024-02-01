<script setup>
  import Dropdown from 'primevue/dropdown';

  const dateOptions = {
    Day: [
      { value: '', label: 'Day', disabled: true },
      { value: '---', label: '---', disabled: true },
      { value: '01', label: '01' },
      { value: '02', label: '02' },
      { value: '03', label: '03' },
      { value: '04', label: '04' },
      { value: '05', label: '05' },
      { value: '06', label: '06' },
      { value: '07', label: '07' },
      { value: '08', label: '08' },
      { value: '09', label: '09' },
      { value: '10', label: '10' },
      { value: '11', label: '11' },
      { value: '12', label: '12' },
      { value: '13', label: '13' },
      { value: '14', label: '14' },
      { value: '15', label: '15' },
      { value: '16', label: '16' },
      { value: '17', label: '17' },
      { value: '18', label: '18' },
      { value: '19', label: '19' },
      { value: '20', label: '20' },
      { value: '21', label: '21' },
      { value: '22', label: '22' },
      { value: '23', label: '23' },
      { value: '24', label: '24' },
      { value: '25', label: '25' },
      { value: '26', label: '26' },
      { value: '27', label: '27' },
      { value: '28', label: '28' },
      { value: '29', label: '29' },
      { value: '30', label: '30' },
      { value: '31', label: '31' }
    ],
    Month: [
      { value: '', label: 'Month', disabled: true },
      { value: '-----', label: '-----', disabled: true },
      { value: '01', label: 'January' },
      { value: '02', label: 'February' },
      { value: '03', label: 'March' },
      { value: '04', label: 'April' },
      { value: '05', label: 'May' },
      { value: '06', label: 'June' },
      { value: '07', label: 'July' },
      { value: '08', label: 'August' },
      { value: '09', label: 'September' },
      { value: '10', label: 'October' },
      { value: '11', label: 'November' },
      { value: '12', label: 'December' }
    ],
    Year: [
      { value: '', label: 'Year', disabled: true },
      { value: '----', label: '----', disabled: true },
      { value: '2012', label: '2012' },
      { value: '2011', label: '2011' },
      { value: '2010', label: '2010' },
      { value: '2009', label: '2009' },
      { value: '2008', label: '2008' },
      { value: '2007', label: '2007' },
      { value: '2006', label: '2006' },
      { value: '2005', label: '2005' },
      { value: '2004', label: '2004' },
      { value: '2003', label: '2003' },
      { value: '2002', label: '2002' },
      { value: '2001', label: '2001' },
      { value: '2000', label: '2000' },
      { value: '1999', label: '1999' },
      { value: '1998', label: '1998' },
      { value: '1997', label: '1997' },
      { value: '1996', label: '1996' },
      { value: '1995', label: '1995' },
      { value: '1994', label: '1994' },
      { value: '1993', label: '1993' },
      { value: '1992', label: '1992' },
      { value: '1991', label: '1991' },
      { value: '1990', label: '1990' },
      { value: '1989', label: '1989' },
      { value: '1988', label: '1988' },
      { value: '1987', label: '1987' },
      { value: '1986', label: '1986' },
      { value: '1985', label: '1985' },
      { value: '1984', label: '1984' },
      { value: '1983', label: '1983' },
      { value: '1982', label: '1982' },
      { value: '1981', label: '1981' },
      { value: '1980', label: '1980' },
      { value: '1979', label: '1979' },
      { value: '1978', label: '1978' },
      { value: '1977', label: '1977' },
      { value: '1976', label: '1976' },
      { value: '1975', label: '1975' },
      { value: '1974', label: '1974' },
      { value: '1973', label: '1973' },
      { value: '1972', label: '1972' },
      { value: '1971', label: '1971' },
      { value: '1970', label: '1970' },
      { value: '1969', label: '1969' },
      { value: '1968', label: '1968' },
      { value: '1967', label: '1967' },
      { value: '1966', label: '1966' },
      { value: '1965', label: '1965' },
      { value: '1964', label: '1964' },
      { value: '1963', label: '1963' },
      { value: '1962', label: '1962' },
      { value: '1961', label: '1961' },
      { value: '1960', label: '1960' },
      { value: '1959', label: '1959' },
      { value: '1958', label: '1958' },
      { value: '1957', label: '1957' },
      { value: '1956', label: '1956' },
      { value: '1955', label: '1955' },
      { value: '1954', label: '1954' },
      { value: '1953', label: '1953' },
      { value: '1952', label: '1952' },
      { value: '1951', label: '1951' },
      { value: '1950', label: '1950' },
      { value: '1949', label: '1949' },
      { value: '1948', label: '1948' },
      { value: '1947', label: '1947' },
      { value: '1946', label: '1946' },
      { value: '1945', label: '1945' },
      { value: '1944', label: '1944' },
      { value: '1943', label: '1943' },
      { value: '1942', label: '1942' },
      { value: '1941', label: '1941' },
      { value: '1940', label: '1940' },
      { value: '1939', label: '1939' },
      { value: '1938', label: '1938' },
      { value: '1937', label: '1937' },
      { value: '1936', label: '1936' },
      { value: '1935', label: '1935' },
      { value: '1934', label: '1934' },
      { value: '1933', label: '1933' },
      { value: '1932', label: '1932' },
      { value: '1931', label: '1931' },
      { value: '1930', label: '1930' },
      { value: '1929', label: '1929' },
      { value: '1928', label: '1928' },
      { value: '1927', label: '1927' },
      { value: '1926', label: '1926' },
      { value: '1925', label: '1925' },
      { value: '1924', label: '1924' },
      { value: '1923', label: '1923' },
      { value: '1922', label: '1922' },
      { value: '1921', label: '1921' },
      { value: '1920', label: '1920' },
      { value: '1919', label: '1919' },
      { value: '1918', label: '1918' },
      { value: '1917', label: '1917' },
      { value: '1916', label: '1916' },
      { value: '1915', label: '1915' },
      { value: '1914', label: '1914' },
      { value: '1913', label: '1913' },
      { value: '1912', label: '1912' },
      { value: '1911', label: '1911' },
      { value: '1910', label: '1910' },
      { value: '1909', label: '1909' },
      { value: '1908', label: '1908' },
      { value: '1907', label: '1907' },
      { value: '1906', label: '1906' },
      { value: '1905', label: '1905' },
      { value: '1904', label: '1904' },
      { value: '1903', label: '1903' },
      { value: '1902', label: '1902' },
      { value: '1901', label: '1901' },
      { value: '1900', label: '1900' },
    ],
  };
</script>

<template>
  <div class="h-screen unselectable">
    <div class="h-full w-full my-auto flex flex-col items-center justify-center">
      <h1 class="text-black font-kanit text-[10rem]">Sign Up</h1>
      <form ref="SubmitForm">
        <div class="relative mb-3">
          <label for="username" class="text-black font-kanit font-semibold text-xl">Username*</label><br>
          <input type="text" id="username" name="username" class="w-[26rem] h-12 p-2 rounded placeholder:text-[#9ca3af] focus:outline-none"
            placeholder="Unique username" v-model="formData.username" required><br>
        </div>
        <div class="relative mb-3">
          <label for="email" class="text-black font-kanit font-semibold text-xl">Email*</label><br>
          <input type="text" id="email" name="email" class="w-[26rem] h-12 p-2 rounded placeholder:text-[#9ca3af] focus:outline-none"
            placeholder="Your email" v-model="formData.email" required>
        </div>
        <div class="relative mb-3">
          <label for="password" class="text-black font-kanit font-semibold text-xl">Password*</label><br>
          <input type="text" id="password" name="password" class="w-[26rem] h-12 p-2 rounded placeholder:text-[#9ca3af] focus:outline-none"
            placeholder="Your password" v-model="formData.password" required><br>
        </div>
        <div class="relative">
          <label class="text-black font-kanit font-semibold text-xl">Date of Birth*</label><br>
          <div class="flex flex-row justify-between">
            <div v-for="(options, label) in dateOptions" :key="label" class="card flex justify-center items-center"> <!--make date of b required-->
              <div v-if="label === 'Day'">
                <Dropdown v-model="formData.day" editable :options="options" optionLabel="label" :placeholder="label" optionDisabled="disabled" class="h-12 w-32 rounded bg-white centered-select-text shadow-none placeholder:text-black"/>
              </div>
              <div v-else-if="label === 'Month'">
                <Dropdown v-model="formData.month" editable :options="options" optionLabel="label" :placeholder="label" optionDisabled="disabled" class="h-12 w-32 rounded bg-white centered-select-text shadow-none"/>
              </div>
              <div v-else-if="label === 'Year'">
                <Dropdown v-model="formData.year" editable :options="options" optionLabel="label" :placeholder="label" optionDisabled="disabled" class="h-12 w-32 rounded bg-white centered-select-text shadow-none"/>
              </div> <!--if its not editable then placeholder isnt centered; but i dont need it to be editable-->
            </div>
          </div>
        </div>
        <div class="text-center mt-10">
          <input type="button" value="Submit" class="bg-black text-yellow text-xl px-8 py-2 rounded font-kanit font-semibold hover:bg-[#141414]" @click="submitForm">
        </div>
      </form> 
    </div>
  </div>
</template>

<style scoped>
.centered-select-text {
  text-align-last:center;
}
</style>

<script>
import { ref } from "vue";

export default {
  data() {
    return {
      formData: {
        username: '',
        email: '',
        password: '',
        day: ref(),
        month: ref(),
        year: ref(),
      },
    };
  },
  methods: {
    submitForm() {
      // Send data to the server

      const form = this.$refs.SubmitForm;
      const formElements = form.elements;

      // Reset custom validity and remove red borders
      for (const element of formElements) {
        element.setCustomValidity('');
        element.style.border = '';
      }

      // Check if the form is valid before submitting
      if (form.checkValidity()) {
        // dont need this check if we do validity check first
        // however ill need to make date fields inputs, so they would be required too
        // otherwise this check will remain
        if (
          this.formData.day && typeof this.formData.day === 'object' &&
          this.formData.month && typeof this.formData.month === 'object' &&
          this.formData.year && typeof this.formData.year === 'object'
        ) {
          this.formData.day = this.formData.day.value;
          this.formData.month = this.formData.month.value;
          this.formData.year = this.formData.year.value;
        }

        fetch('http://127.0.0.1:8000/signup', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.formData),
        })
        .then(response => {
          if (!response.ok) {
            // Handle non-successful response codes here
            if (response.status === 422) {
              // Handle 422 Unprocessable Entity
              return response.json().then(errorData => {
                // Tell them that email form is incorrect
                throw new Error(`Validation error: ${JSON.stringify(errorData)}`);
              });
            } else {
              // Handle other non-successful response codes
              throw new Error(`Server error: ${response.status}`);
            }
          }
          return response.json();
        })
        .then(data => {
          localStorage.setItem("token", JSON.stringify(data));
          console.log(data);
          console.log(localStorage.getItem("token"));
        })
        .catch(error => console.error('Error:', error));

        console.log("posted");
      } else {
        // Highlight invalid fields with red borders
        for (const element of formElements) {
          if (!element.checkValidity()) {
            // Some styling here or whatever
            element.setCustomValidity('Please fill in this field');
            element.style.border = '0.1em solid red';
          }
        }
      }
    },
  },
};
</script>