<!--<script setup lang="ts">

import { ref } from 'vue'

import { usePotiah, ScrollView, ScrollComponent } from 'potiah'

const flag = ref(true)
const duration = ref(1.4)

const { scrollTo, potiah, direction, isScrolling } = usePotiah()

const zero = ref<InstanceType<typeof ScrollComponent> | null>(null)
const zero1 = ref<InstanceType<typeof ScrollComponent> | null>(null)
const blank = ref<HTMLElement>()

</script>


<template>  
  <main>
    <ScrollView :duration="duration" css-direction root>
      <ScrollComponent id="top" is="section" class="zero" ref="zero">
        Scroll comp text!!!
      </ScrollComponent>
      <div class="hello">
        <h1>Hello World From Sam</h1>
      </div>

      <div id="sticky" class="second" data-scroll data-scroll-speed="0.2" :data-flag="flag">
        <h1
          data-scroll
          data-scroll-sticky
          data-scroll-target="#sticky"
        >
          Sticky scroll example
        </h1>
        <p>Placeholders Placeholders</p>
        <p>Placeholders Placeholders</p>
        <p>Placeholders Placeholders</p>
        <p>Placeholders Placeholders</p>
      </div>

      <div class="third">
        <h1>Vertical Parallax scroll</h1>
        <h1>Horizontal Parallax Scroll</h1>
      </div>
      <div id="blank" class="blank" ref="blank"></div>
      <ScrollComponent
        in-view-class="test-in-view-class"
        repeat
        :style="{ height: '25vh', background: 'blue' }"
      >dirty bastard </ScrollComponent>
    </ScrollView>
  </main>
</template>

<script>
</script>

<style>
section {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: xx-large;
}
.hello {
  background-color: red;
  width: 100vw;
  background-image: url("/src/assets/background.png");
  background-size: cover;
  color: rgba(0, 0, 0, 0.745);
}
.third {
  background-color: greenyellow;
}
#sticky {
  background-color: black;
  padding: 50px;
}
.scroll-into-view {
  background-color: black;
  color: white;
}
</style>-->


<template>
  <div class="card flex justify-content-center">
      <Dropdown v-model="selectedCity" :options="cities" optionLabel="label" placeholder="Select a City" class="w-96 md:w-14rem" />
  </div>
</template>

<script setup>
  import { ref } from "vue";
  import Dropdown from 'primevue/dropdown';

  const selectedCity = ref();
  const cities = ref([
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
  ]);
</script>




