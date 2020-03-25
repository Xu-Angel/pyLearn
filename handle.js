const fs = require('fs')

const data = [...fs.readFileSync('out.txt', {encoding: 'utf-8'})]
const set = [...new Set(data)]
const ar = []
set.forEach(v => {
  const cur = v.trim()
  let count = 0
  data.forEach(V => {
    if (cur === V.trim()) {
      count += 1
    }
  })
  if (cur.length > 1) {
    ar.push({ word: cur, count })
  }
})
// ar.sort((a, b) => {return (a.count - b.count)})
fs.writeFileSync('res.txt', JSON.stringify(ar))