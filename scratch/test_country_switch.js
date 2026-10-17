const fs = require('fs');

const jsContent = fs.readFileSync('frontend/app.js', 'utf8');

// Basic syntax parse check
try {
  new Function(jsContent);
  console.log('✅ frontend/app.js syntax parsed successfully with no errors!');
} catch (err) {
  console.error('❌ Syntax error in frontend/app.js:', err);
  process.exit(1);
}

// Verify critical logic strings
const checks = [
  { name: 'currentBoundingBox updated on country change', test: jsContent.includes('currentBoundingBox = countryMeta.bbox') },
  { name: 'zoneSelect synced in onRegionSelected', test: jsContent.includes('zoneSelect.querySelector(`option[value="${region.id}"]`)') },
  { name: 'zoneSelect updated in loadAndPopulateRegions', test: jsContent.includes('if (zoneSelect) zoneSelect.value = target.id;') },
  { name: 'zoneSelect listener checks active country regions', test: jsContent.includes('const activeRegions = countryRegionsCache[currentCountryCode] || [];') }
];

checks.forEach(c => {
  if (c.test) {
    console.log(`✅ Passed: ${c.name}`);
  } else {
    console.error(`❌ Failed: ${c.name}`);
    process.exit(1);
  }
});
console.log('All verification checks passed!');
