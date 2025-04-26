const fs = require('fs-extra');
const path = require('path');
const sharp = require('sharp');

// Directory containing the images
const inputDir = path.join(__dirname, './dist/assets/meals-n');
const outputDir = path.join(__dirname, './dist/assets/meals-n-processed');

// Ensure the output directory exists
fs.ensureDirSync(outputDir);

// Batch size to process images
const BATCH_SIZE = 10;

// Function to process a batch of images
async function processBatch(files) {
  const promises = files.map((file) => {
    const inputFilePath = path.join(inputDir, file);
    const outputFilePath = path.join(outputDir, `${path.parse(file).name}.png`);

    if (/\.(jpg|jpeg|png|webp)$/i.test(file)) {
      return sharp(inputFilePath)
        .resize(720, 290, { fit: 'contain' })
        .toFile(outputFilePath)
        .then(() => console.log(`Processed: ${file} -> ${outputFilePath}`))
        .catch((err) => console.error(`Error processing ${file}:`, err));
    } else {
      console.log(`Skipping non-image file: ${file}`);
      return Promise.resolve(); // Skip non-image files
    }
  });

  await Promise.all(promises); // Wait for all files in the batch to finish
}

// Main function to process all images in batches
async function processImages() {
  try {
    const files = await fs.readdir(inputDir);

    for (let i = 0; i < files.length; i += BATCH_SIZE) {
      const batch = files.slice(i, i + BATCH_SIZE);
      console.log(`Processing batch: ${i / BATCH_SIZE + 1}`);
      await processBatch(batch); // Process the current batch
    }

    console.log('All images processed successfully!');
  } catch (err) {
    console.error('Error reading input directory:', err);
  }
}

// Start processing
processImages();