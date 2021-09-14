//
//  ComplicationController.swift
//  WatchToolProject Extension
//
//  Created by MEI YIN LO on 2021/6/20.
//

import ClockKit


class ComplicationController: NSObject, CLKComplicationDataSource {
    
    // MARK: - Complication Configuration

    func getComplicationDescriptors(handler: @escaping ([CLKComplicationDescriptor]) -> Void) {
        let descriptors = [
           // CLKComplicationDescriptor(identifier: "complication", displayName: "ToolProject", supportedFamilies: CLKComplicationFamily.allCases)
            CLKComplicationDescriptor(identifier: "utilitarianSmall", displayName: "utilitarianSmall", supportedFamilies:[ CLKComplicationFamily.utilitarianSmall]),
            CLKComplicationDescriptor(identifier: "utilitarianSmallFlat", displayName: "utilitarianSmallFlat", supportedFamilies:[ CLKComplicationFamily.utilitarianSmallFlat]) ,
            CLKComplicationDescriptor(identifier: "utilitarianLarge", displayName: "utilitarianLarge", supportedFamilies:[ CLKComplicationFamily.utilitarianLarge]),
            CLKComplicationDescriptor(identifier: "circularSmall", displayName: "circularSmall", supportedFamilies:[ CLKComplicationFamily.circularSmall]),
            CLKComplicationDescriptor(identifier: "extraLarge", displayName: "extraLarge", supportedFamilies:[ CLKComplicationFamily.extraLarge]),
            CLKComplicationDescriptor(identifier: "graphicCorner", displayName: "graphicCorner", supportedFamilies:[ CLKComplicationFamily.graphicCorner]),
            CLKComplicationDescriptor(identifier: "graphicCircular", displayName: "graphicCircular", supportedFamilies:[ CLKComplicationFamily.graphicCircular]),
            CLKComplicationDescriptor(identifier: "graphicBezel", displayName: "graphicBezel", supportedFamilies:[ CLKComplicationFamily.graphicBezel]),
            CLKComplicationDescriptor(identifier: "graphicRectangular", displayName: "graphicRectangular", supportedFamilies:[ CLKComplicationFamily.graphicRectangular]),
            CLKComplicationDescriptor(identifier: "graphicExtraLarge", displayName: "graphicExtraLarge", supportedFamilies:[ CLKComplicationFamily.graphicExtraLarge]),
            CLKComplicationDescriptor(identifier: "modularSmall", displayName: "modularSmall", supportedFamilies:[ CLKComplicationFamily.modularSmall]),
            CLKComplicationDescriptor(identifier: "modularLarge", displayName: "modularLarge", supportedFamilies:[ CLKComplicationFamily.modularLarge]),
            // Multiple complication support can be added here with more descriptors
        ]
        
        // Call the handler with the currently supported complication descriptors
        handler(descriptors)
    }
    
    func handleSharedComplicationDescriptors(_ complicationDescriptors: [CLKComplicationDescriptor]) {
        // Do any necessary work to support these newly shared complication descriptors
    }

    // MARK: - Timeline Configuration
    
    func getTimelineEndDate(for complication: CLKComplication, withHandler handler: @escaping (Date?) -> Void) {
        // Call the handler with the last entry date you can currently provide or nil if you can't support future timelines
        handler(nil)
    }
    
    func getPrivacyBehavior(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationPrivacyBehavior) -> Void) {
        // Call the handler with your desired behavior when the device is locked
        handler(.showOnLockScreen)
    }

    // MARK: - Timeline Population
    
    func getCurrentTimelineEntry(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTimelineEntry?) -> Void) {
        // Call the handler with the current timeline entry
        //handler(nil)
        if complication.family == .circularSmall{
            handler(CLKComplicationTimelineEntry(date: Date(), complicationTemplate: CLKComplicationTemplateCircularSmallSimpleText(textProvider: CLKSimpleTextProvider(text: "circularSmall", shortText: "cs"))))
        }
        if complication.family == .utilitarianSmallFlat{
            handler(CLKComplicationTimelineEntry(date: Date(), complicationTemplate: CLKComplicationTemplateUtilitarianSmallFlat(textProvider: CLKSimpleTextProvider(text: "utilitarianSmallFlat", shortText: "usf"))))
        }
        if complication.family == .utilitarianSmall{
            handler(CLKComplicationTimelineEntry(date: Date(), complicationTemplate: CLKComplicationTemplateUtilitarianSmallRingText(textProvider: CLKSimpleTextProvider(text: "utilitarianSmall", shortText: "us"), fillFraction: 0.8, ringStyle: .closed )))
        }
        if complication.family == .utilitarianLarge{
            handler(CLKComplicationTimelineEntry(date: Date(), complicationTemplate: CLKComplicationTemplateUtilitarianLargeFlat(textProvider: CLKSimpleTextProvider(text: "utilitarianLarge", shortText: "ul")  )))
        }
        if complication.family == .graphicCorner{
            handler(CLKComplicationTimelineEntry(date: Date(), complicationTemplate: CLKComplicationTemplateGraphicCornerStackText(innerTextProvider: CLKSimpleTextProvider(text: "graphicCorner", shortText: "gco"), outerTextProvider:  CLKSimpleTextProvider(text: "graphicCorner", shortText: "gco")  )))
        }
        if complication.family == .graphicCircular{
            handler(CLKComplicationTimelineEntry(date: Date(), complicationTemplate: CLKComplicationTemplateGraphicCircularStackText(  line1TextProvider: CLKSimpleTextProvider(text: "graphicCircular", shortText: "gci"), line2TextProvider:  CLKSimpleTextProvider(text: "graphicCircular", shortText: "gci")  )))
        }
        if complication.family == .graphicBezel{
            handler(CLKComplicationTimelineEntry(date: Date(), complicationTemplate: CLKComplicationTemplateGraphicBezelCircularText(circularTemplate: CLKComplicationTemplateGraphicCircularStackText(  line1TextProvider: CLKSimpleTextProvider(text: "graphicBezel", shortText: "gb"), line2TextProvider:  CLKSimpleTextProvider(text: "graphicBezel", shortText: "gb")  ), textProvider:   CLKSimpleTextProvider(text: "graphicBezel", shortText: "gb")  )))
        }
        if complication.family == .graphicRectangular{
            handler(CLKComplicationTimelineEntry(date: Date(), complicationTemplate: CLKComplicationTemplateGraphicRectangularStandardBody(  headerTextProvider:   CLKSimpleTextProvider(text: "graphicRectangular", shortText: "gr"), body1TextProvider:  CLKSimpleTextProvider(text: "graphicRectangular", shortText: "gr")  )))
        }
        if complication.family == .graphicExtraLarge{
            handler(CLKComplicationTimelineEntry(date: Date(), complicationTemplate: CLKComplicationTemplateGraphicExtraLargeCircularStackText(  line1TextProvider:   CLKSimpleTextProvider(text: "graphicRectangular", shortText: "gr"), line2TextProvider:  CLKSimpleTextProvider(text: "graphicRectangular", shortText: "gr")  )))
        }
        if complication.family == .modularSmall{
            handler(CLKComplicationTimelineEntry(date: Date(), complicationTemplate: CLKComplicationTemplateModularSmallSimpleText(textProvider: CLKSimpleTextProvider(text: "modularSmall", shortText: "ms")  )))
        }
        if complication.family == .modularLarge{
            handler(CLKComplicationTimelineEntry(date: Date(), complicationTemplate: CLKComplicationTemplateModularLargeStandardBody(headerTextProvider: CLKSimpleTextProvider(text: "modularLarge", shortText: "ml") , body1TextProvider:   CLKSimpleTextProvider(text: "modularLarge", shortText: "ml")  )))
        }
    }
    
    func getTimelineEntries(for complication: CLKComplication, after date: Date, limit: Int, withHandler handler: @escaping ([CLKComplicationTimelineEntry]?) -> Void) {
        // Call the handler with the timeline entries after the given date
        handler(nil)
    }

    // MARK: - Sample Templates
    
    func getLocalizableSampleTemplate(for complication: CLKComplication, withHandler handler: @escaping (CLKComplicationTemplate?) -> Void) {
        // This method will be called once per supported complication, and the results will be cached
        if complication.family == .circularSmall{
            handler(  CLKComplicationTemplateCircularSmallSimpleText(textProvider: CLKSimpleTextProvider(text: "circularSmall", shortText: "cs")))
        }
        if complication.family == .utilitarianSmallFlat{
            handler( CLKComplicationTemplateUtilitarianSmallFlat(textProvider: CLKSimpleTextProvider(text: "utilitarianSmallFlat", shortText: "usf")))
        }
        if complication.family == .utilitarianSmall{
            handler(  CLKComplicationTemplateUtilitarianSmallRingText(textProvider: CLKSimpleTextProvider(text: "utilitarianSmall", shortText: "us"), fillFraction: 0.8, ringStyle: .closed ))
        }
        if complication.family == .utilitarianLarge{
            handler( CLKComplicationTemplateUtilitarianLargeFlat(textProvider: CLKSimpleTextProvider(text: "utilitarianLarge", shortText: "ul")  ))
        }
        if complication.family == .graphicCorner{
            handler( CLKComplicationTemplateGraphicCornerStackText(innerTextProvider: CLKSimpleTextProvider(text: "graphicCorner", shortText: "gco"), outerTextProvider:  CLKSimpleTextProvider(text: "graphicCorner", shortText: "gco")  ))
        }
        if complication.family == .graphicCircular{
            handler( CLKComplicationTemplateGraphicCircularStackText(  line1TextProvider: CLKSimpleTextProvider(text: "graphicCircular", shortText: "gci"), line2TextProvider:  CLKSimpleTextProvider(text: "graphicCircular", shortText: "gci")  ))
        }
        if complication.family == .graphicBezel{
            handler(  CLKComplicationTemplateGraphicBezelCircularText(circularTemplate: CLKComplicationTemplateGraphicCircularStackText(  line1TextProvider: CLKSimpleTextProvider(text: "graphicBezel", shortText: "gb"), line2TextProvider:  CLKSimpleTextProvider(text: "graphicBezel", shortText: "gb")  ), textProvider:   CLKSimpleTextProvider(text: "graphicBezel", shortText: "gb")  ))
        }
        if complication.family == .graphicRectangular{
            handler(  CLKComplicationTemplateGraphicRectangularStandardBody(  headerTextProvider:   CLKSimpleTextProvider(text: "graphicRectangular", shortText: "gr"), body1TextProvider:  CLKSimpleTextProvider(text: "graphicRectangular", shortText: "gr")  ))
        }
        if complication.family == .graphicExtraLarge{
            handler(  CLKComplicationTemplateGraphicExtraLargeCircularStackText(  line1TextProvider:   CLKSimpleTextProvider(text: "graphicRectangular", shortText: "gr"), line2TextProvider:  CLKSimpleTextProvider(text: "graphicRectangular", shortText: "gr")  ))
        }
        if complication.family == .modularSmall{
            handler( CLKComplicationTemplateModularSmallSimpleText(textProvider: CLKSimpleTextProvider(text: "modularSmall", shortText: "ms")  ))
        }
        if complication.family == .modularLarge{
            handler(  CLKComplicationTemplateModularLargeStandardBody(headerTextProvider: CLKSimpleTextProvider(text: "modularLarge", shortText: "ml") , body1TextProvider:   CLKSimpleTextProvider(text: "modularLarge", shortText: "ml")  ))
        }
    }
}
